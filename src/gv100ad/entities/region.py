##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from gv100ad.entities.base_record import BaseRecord

class Region(BaseRecord):
    def __init__(self, line):
        """
        Initializes a new instance of the Region class.
        
        Args:
            line (str): A text row with Satzart 30.
        """
        super().__init__(line)
        
        self.regional_code = line[10:15].rstrip()
        self.administrative_headquarters = line[72:122].rstrip()

    def __repr__(self):
        return (f"Region(Name={self.name}, RegionalCode={self.regional_code}, "
                f"AdministrativeHeadquarters={self.administrative_headquarters}, TimeStamp={self.timestamp})")
