##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from gv100ad.entities.base_record import BaseRecord
from gv100ad.entities.municipal_association_type import MunicipalAssociationType

class MunicipalAssociation(BaseRecord):
    """
    A municipal association (Gemeindeverband) from GV100AD

    Attributes:
        regional_code (str): Regionalschlüssel (EF3)
        association (str): Gemeindeverband (EF4)
        administrative_headquarters (str): Verwaltungssitz des Gemeindeverbandes (EF6)
        type (MunicipalAssociationType): Kennzeichen (EF7)
    """
    
    regional_code: str
    association: str
    administrative_headquarters: str
    type: MunicipalAssociationType

    def __init__(self, line):
        """
        Initializes a new instance of the MunicipalAssociation class.
        
        Args:
            line (str): A text row with Satzart 50.
        """
        super().__init__(line)

        self.regional_code = line[10:15]
        self.association = line[18:22]
        self.administrative_headquarters = line[72:122].rstrip()
        association_type_str = line[122:124].strip()
        self.type = MunicipalAssociationType(int(association_type_str) if association_type_str else 0)

    def __repr__(self):
        return (f"MunicipalAssociation(Name={self.name}, RegionalCode={self.regional_code}, "
                f"Association={self.association}, AdministrativeHeadquarters={self.administrative_headquarters}, "
                f"Type={self.type}, TimeStamp={self.timestamp})")
