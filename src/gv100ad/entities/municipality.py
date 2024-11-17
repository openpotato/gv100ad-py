##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from gv100ad.entities.base_record import BaseRecord
from gv100ad.entities.municipality_type import MunicipalityType

class Municipality(BaseRecord):
    """
    A municipality (Gemeinde) from GV100AD

    Attributes:
        regional_code (str): Regionalschlüssel (EF3)
        association (str): Gemeindeverband (EF4)
        type (MunicipalityType): Kennzeichen (EF7)
        area (int): Area in hectares (EF8)
        inhabitants (int): Total population (EF9)
        inhabitants_male (int): Male population (EF10)
        postal_code (str): Postalcode (if there are multiple postcodes, it's the postalcode of the Verwaltungssitz) (EF12U1)
        multiple_postal_codes (bool): Multiple postcodes available? (EF12U2)
        tax_office_district (str): Finanzamtsbezirk (EF14)
        higher_regional_court_district (str): Oberlandesgerichtsbezirk (EF15U1)
        regional_court_district (str): Landgerichtsbezirk (EF15U2)
        local_court_district (str): Amtsgerichtsbezirk (EF15U3)
        employment_agency_district (str): Arbeitsagenturbezirk (EF16)
    """
    
    regional_code: str
    association: str
    type: MunicipalityType
    area: int
    inhabitants: int
    inhabitants_male: int
    postal_code: str
    multiple_postal_codes: bool
    tax_office_district: str
    higher_regional_court_district: str
    regional_court_district: str
    local_court_district: str
    employment_agency_district: str

    def __init__(self, line):
        """
        Initializes a new instance of the Municipality class.
        
        Args:
            line (str): A text row with Satzart 60.
        """
        super().__init__(line)  

        self.regional_code = line[10:18]
        self.association = line[18:22]
        self.type = MunicipalityType(int(line[122:124].strip() or 0))
        self.area = int(line[128:139].strip())
        self.inhabitants = int(line[139:150].strip())
        self.inhabitants_male = int(line[150:161].strip())
        self.postal_code = line[165:170].strip()
        self.multiple_postal_codes = bool(line[170:175].strip())
        self.tax_office_district = line[177:181].strip()
        self.higher_regional_court_district = line[181:182].strip()
        self.regional_court_district = line[182:183].strip()
        self.local_court_district = line[183:185].strip()
        self.employment_agency_district = line[185:190].strip()

    def __repr__(self):
        return (f"Municipality(Name={self.name}, RegionalCode={self.regional_code}, "
                f"Association={self.association}, Type={self.type}, Area={self.area}, "
                f"Inhabitants={self.inhabitants}, InhabitantsMale={self.inhabitants_male}, "
                f"PostalCode={self.postal_code}, MultiplePostalCodes={self.multiple_postal_codes}, "
                f"TaxOfficeDistrict={self.tax_office_district}, HigherRegionalCourtDistrict={self.higher_regional_court_district}, "
                f"RegionalCourtDistrict={self.regional_court_district}, LocalCourtDistrict={self.local_court_district}, "
                f"EmploymentAgencyDistrict={self.employment_agency_district}, TimeStamp={self.timestamp})")
