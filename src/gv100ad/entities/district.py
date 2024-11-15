##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from gv100ad.entities.base_record import BaseRecord
from gv100ad.entities.district_type import DistrictType

class District(BaseRecord):
    """
    A district (Kreis) from GV100AD

    Attributes:
        regional_code (str): Regionalschlüssel (EF3)
        administrative_headquarters (str): Sitz der Kreisverwaltung (EF6)
        type (DistrictType): Kennzeichen (EF7)
    """
    
    regional_code: str
    administrative_headquarters: str
    type: DistrictType

    def __init__(self, line):
        """
        Initializes a new instance of the District class.

        Args:
            line (str): A text row with Satzart 40.
        """        
        super().__init__(line)
        
        self.regional_code = line[10:15]
        self.administrative_headquarters = line[72:122].rstrip()
        district_type_str = line[122:124].strip()
        self.type = DistrictType(int(district_type_str) if district_type_str else 0)

    def __repr__(self):
        return (f"District(Name={self.name}, RegionalCode={self.regional_code}, "
                f"AdministrativeHeadquarters={self.administrative_headquarters}, Type={self.type}, "
                f"TimeStamp={self.timestamp})")
