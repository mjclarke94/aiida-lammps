import numpy as np

from aiida_lammps.data.pot_plugins.base_plugin import PotentialAbstract


class Buckingham(PotentialAbstract):
    """Class for creation of Lennard-Jones potential inputs."""

    def validate_data(self, data):
        """Validate the input data."""
        pass

    def get_external_content(self):
        return None

    def get_input_potential_lines(self):

        lammps_input_text = "pair_style  buck/coul/long 12.0\n"

        lammps_input_text += "pair_coeff * * 0.0 1.0 0.0\n"

        for key in sorted(self.data.keys()):
            lammps_input_text += "pair_coeff {} {}\n".format(key, self.data[key])

        lammps_input_text += 'kspace_style pppm 1e-05\n'

        return lammps_input_text

    @property
    def allowed_element_names(self):
        return None

    @property
    def atom_style(self):
        return "charge"

    @property
    def default_units(self):
        return "metal"
    @property
    def charge_dict(self):
        return {'Li': 1, 'O': -2, 'Cl': -1}
