"""
main.py Define person class to poll
Copyright (C) 2019 Jorge Antonio Camarena Pliego (camarenapliego@gmail.com)
Keshava Tonathiu Sanchez Barbosa (keshava.t.s.b@gmail.com)
Stephany Dzoara Vargas Mier (stephanydvm@comunidad.unam.mx)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

class person:
    def __init__(self, age = 18, sex, income = 1825, education = 12, race, religion, 
                marital_status, sexual_orientation, children = 0, security_percetion = 10):
        self.age = age #years
        self.sex = sex #M, F, I
        self.income = income #dollars per year
        self.education = education #years
        self.race = race #
        self.religion = religion #
        self.marital_status = marital_status
        self.sexual_orientation = sexual_orientation
        self.children = children
        self.security_percetion = security_percetion