##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from gv100ad.entities.base_record import BaseRecord

class FederalState(BaseRecord):
    """
    A federal state (Bundesland) from GV100AD

    Attributes:
        regional_code (str): Regionalschlüssel (EF3)
        seat_of_government (str): Sitz der Landesregierung (EF6)
    """
    
    regional_code: str
    seat_of_government: str

    def __init__(self, line):
        """
        Initializes a new instance of the FederalState class.
        
        Args:
            line (str): A text row with Satzart 10.
        """
        super().__init__(line)

        self.regional_code = line[10:12]
        self.seat_of_government = line[72:122].rstrip()

    def __repr__(self):
        return (f"FederalState(Name={self.name}, RegionalCode={self.regional_code}, "
                f"SeatOfGovernment={self.seat_of_government}, TimeStamp={self.timestamp})")
