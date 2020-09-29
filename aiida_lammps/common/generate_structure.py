""" creation of the structure file content
"""
# import ase
import numpy as np


def transform_cell(cell):
    """transform the cell to an orientation, compatible with LAMMPS

    LAMMPS requires the simulation cell to be in the format of a
    lower triangular matrix (right-handed basis).
    Therefore the cell and positions may require rotation and inversion.
    See https://lammps.sandia.gov/doc/Howto_triclinic.html

    :param cell: (3x3) lattice
    :returns: (new_cell, transform)

    """
    cell = np.array(cell)
    transform, upper_tri = np.linalg.qr(cell.T, mode="complete")
    new_cell = np.transpose(upper_tri)

    # LAMMPS also requires positive values on the diagonal of the,
    # so invert cell if necessary
    inversion = np.eye(3)
    for i in range(3):
        if new_cell[i][i] < 0.0:
            inversion[i][i] = -1.0
    new_cell = np.dot(inversion, new_cell.T).T
    transform = np.dot(transform, inversion.T).T

    return new_cell, transform


def generate_lammps_structure(
    structure,
    atom_style="atomic",
    charge_dict=None,
    round_dp=None,
    docstring="generated by aiida_lammps",
):
    """create lammps input structure file content

    Parameters
    ----------
    structure: StructureData
        the structure to use
    atom_style: str
        the atomic style
    charge_dict: dict
        mapping of atom kind_name to charge
    round_dp: None or int
        round output values to a number of decimal places (used for testing)
    docstring : str
        docstring to put at top of file

    Returns
    -------
    str: content
        the structure file content
    numpy.array: transform
        the transformation matrix applied to the structure cell and coordinates

    """
    if atom_style not in ["atomic", "charge"]:
        raise ValueError(
            "atom_style must be in ['atomic', 'charge'], not '{}'".format(atom_style)
        )
    if charge_dict is None:
        charge_dict = {}

    # mapping of atom kind_name to id number
    kind_name_id_map = {}
    for site in structure.sites:
        if site.kind_name not in kind_name_id_map:
            kind_name_id_map[site.kind_name] = len(kind_name_id_map) + 1
    # mapping of atom kind_name to mass
    kind_mass_dict = {kind.name: kind.mass for kind in structure.kinds}

    filestring = ""
    filestring += "# {}\n\n".format(docstring)
    filestring += "{0} atoms\n".format(len(structure.sites))
    filestring += "{0} atom types\n\n".format(len(kind_name_id_map))

    atoms = structure.get_ase()
    cell, coord_transform = transform_cell(atoms.cell)
    positions = np.transpose(np.dot(coord_transform, np.transpose(atoms.positions)))

    if round_dp:
        cell = np.round(cell, round_dp) + 0.0
        positions = np.round(positions, round_dp) + 0.0

    filestring += "0.0 {0:20.10f} xlo xhi\n".format(cell[0][0])
    filestring += "0.0 {0:20.10f} ylo yhi\n".format(cell[1][1])
    filestring += "0.0 {0:20.10f} zlo zhi\n".format(cell[2][2])
    filestring += "{0:20.10f} {1:20.10f} {2:20.10f} xy xz yz\n\n".format(
        cell[1][0], cell[2][0], cell[2][1]
    )

    filestring += "Masses\n\n"
    for kind_name in sorted(list(kind_name_id_map.keys())):
        filestring += "{0} {1:20.10f} \n".format(
            kind_name_id_map[kind_name], kind_mass_dict[kind_name]
        )
    filestring += "\n"

    filestring += "Atoms\n\n"

    for site_index, (pos, site) in enumerate(zip(positions, structure.sites)):

        kind_id = kind_name_id_map[site.kind_name]

        if atom_style == "atomic":
            filestring += "{0} {1} {2:20.10f} {3:20.10f} {4:20.10f}\n".format(
                site_index + 1, kind_id, pos[0], pos[1], pos[2]
            )
        elif atom_style == "charge":
            charge = charge_dict.get(site.kind_name, 0.0)
            filestring += "{0} {1} {2} {3:20.10f} {4:20.10f} {5:20.10f}\n".format(
                site_index + 1, kind_id, charge, pos[0], pos[1], pos[2]
            )
        else:
            raise ValueError("atom_style unknown: {}".format(atom_style))

    return filestring, coord_transform
