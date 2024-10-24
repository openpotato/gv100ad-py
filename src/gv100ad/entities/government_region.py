##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from gv100ad.entities.base_record import BaseRecord

class GovernmentRegion(BaseRecord):
    def __init__(self, line):
        """
        Initializes a new instance of the GovernmentRegion class.
        :param line: A text row with Satzart 20.
        """
        super().__init__(line)
        
        self.regional_code = line[10:13]
        self.administrative_headquarters = line[72:122].rstrip()

    def __repr__(self):
        return (f"GovernmentRegion(Name={self.name}, RegionalCode={self.regional_code}, "
                f"AdministrativeHeadquarters={self.administrative_headquarters}, "
                f"TimeStamp={self.timestamp})")