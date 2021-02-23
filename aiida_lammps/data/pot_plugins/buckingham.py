import numpy as np

from aiida_lammps.data.pot_plugins.base_plugin import PotentialAbstract


class Buckingham(PotentialAbstract):
    """Class for creation of Buckingham potential inputs."""

    def __init__(self, data):
        super().__init__(data)
        self._charge_dict = data.get("charge_dict", None)
        self._kind_map = data.get("kind_map", None)

    def validate_data(self, data):
        """Validate the input data."""
        pass

    def get_external_content(self):
        return None

    def get_input_potential_lines(self):

        lammps_input_text = "pair_style  buck/coul/long 12.0\n"

        lammps_input_text += "pair_coeff * * 0.0 1.0 0.0\n"

        buckingham_potentials = self.data["2-body"]

        for key, val in sorted(
            buckingham_potentials.items(),
            key=lambda kv: sorted([self.kind_map[i] for i in kv[0]]),
        ):

            kinds = sorted(key, key=lambda x: self.kind_map[x])
            ids = [self.kind_map[kind] for kind in kinds]

            # Write coefficient part of line
            s = f"pair_coeff {ids[0]} {ids[1]} {val['A']:14.6f} {val['rho']:9.6f} {val['C']:10.6f}"

            # Add comment giving id -> kind map

            s += f" # {kinds[0]:<2} {kinds[1]:<2}\n"

            lammps_input_text += s

        lammps_input_text += "kspace_style pppm 1e-05\n"

        return lammps_input_text

    @property
    def allowed_element_names(self):
        return None

    @property
    def atom_style(self):
        if self.charge_dict:
            return "charge"
        return "atomic"

    @property
    def default_units(self):
        return "metal"

    @property
    def charge_dict(self):
        return self._charge_dict

    @charge_dict.setter
    def charge_dict(self, value):
        self._charge_dict = value

    @property
    def kind_map(self):
        return self._kind_map

    @kind_map.setter
    def kind_map(self, value):
        self._kind_map = value
