"""
RaiderPropellantCharacterization - Program for interpretation of subscale static fire data to characterize solid rocket motor propellants.
Copyright (C) 2026 Kyle Markel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

class TestFire:
    # def __init__(self, filename, sheetnames, psmoothing, tsmoothing, fireIndex, pressUnits, thrustUnits, geomUnits, throatUnits, geometry, throat, massUnits, mass, densityUnits, density, dat, calculation):
    #     self._filename = filename
    #     self._sheetnames = sheetnames
    #     self._fireIndex = fireIndex
    #     self._pressUnits = pressUnits
    #     self._thrustUnits = thrustUnits
    #     self._geomUnits = geomUnits
    #     self._throatUnits = throatUnits
    #     self._geometry = geometry
    #     self._throat = throat
    #     self._massUnits = massUnits
    #     self._mass = mass
    #     self._densityUnits = densityUnits
    #     self._density = density
    #     self._dat = dat
    #     self._calculation = calculation
    
    def __init__(self):
        pass
    
    #getters and setters

    def get_filename(self):
        return self._filename

    def set_filename(self, value):
        self._filename = value

    def get_sheetnames(self):
        return self._sheetnames

    def set_sheetnames(self, value):
        self._sheetnames = value

    def get_psmoothing(self):
        return self._psmoothing

    def set_psmoothing(self, value):
        self._psmoothing = value

    def get_tsmoothing(self):
        return self._tsmoothing

    def set_tsmoothing(self, value):
        self._tsmoothing = value

    def get_fireIndex(self):
        return self._fireIndex

    def set_fireIndex(self, value):
        self._fireIndex = value

    def get_pressUnits(self):
        return self._pressUnits

    def set_pressUnits(self, value):
        self._pressUnits = value

    def get_thrustUnits(self):
        return self._thrustUnits

    def set_thrustUnits(self, value):
        self._thrustUnits = value

    def get_geomUnits(self):
        return self._geomUnits

    def set_geomUnits(self, value):
        self._geomUnits = value

    def get_throatUnits(self):
        return self._throatUnits

    def set_throatUnits(self, value):
        self._throatUnits = value

    def get_geometry(self):
        return self._geometry

    def set_geometry(self, value):
        self._geometry = value

    def get_throat(self):
        return self._throat

    def set_throat(self, value):
        self._throat = value
    
    def get_massUnits(self):
        return self._massUnits

    def set_massUnits(self, value):
        self._massUnits = value
    
    def get_mass(self):
        return self._mass

    def set_mass(self, value):
        self._mass = value

    def get_densityUnits(self):
        return self._densityUnits

    def set_densityUnits(self, value):
        self._densityUnits = value

    def get_density(self):
        return self._density

    def set_density(self, value):
        self._density = value

    def get_dat(self):
        return self._dat

    def set_dat(self, value):
        self._dat = value
    
    def get_calculation(self):
        return self._calculation

    def set_calculation(self, value):
        self._calculation = value
