##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from enum import Enum

class MunicipalAssociationType(Enum):
    """
    Municipal association type (Gemeindeverbandskennzeichen) 
    """
    NONE = 0
    VERBANDSFREIE_GEMEINDE = 50
    AMT = 51
    SAMTGEMEINDE = 52
    VERBANDSGEMEINDE = 53
    VERWALTUNGSGEMEINSCHAFT = 54
    KIRCHSPIELSLANDGEMEINDE = 55
    VERWALTUNGSVERBAND = 56
    VG_TRAEGERMODELL = 57
    ERFUELLENDE_GEMEINDE = 58
