##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from enum import Enum

class DistrictType(Enum):
    """
    District type (Kreiskennzeichen)
    """
    NONE = 0
    KREISFREIE_STADT = 41
    STADTKREIS = 42
    KREIS = 43
    LANDKREIS = 44
    REGIONALVERBAND = 45
