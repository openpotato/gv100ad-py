##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from enum import Enum

class MunicipalityType(Enum):
    """
    Municipality type (Gemeindekennzeichen)
    """
    NONE = 0
    MARKT = 60
    KREISFREIE_STADT = 61
    STADTKREIS = 62
    STADT = 63
    KREISANGEHOERIGE_GEMEINDE = 64
    GEMEINDEFREIES_GEBIET_BEWOHNT = 65
    GEMEINDEFREIES_GEBIET_UNBEWOHNT = 66
    GROSSE_KREISSTADT = 67
