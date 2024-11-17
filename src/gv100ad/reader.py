##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from typing import Iterable, AsyncIterator
from gv100ad.entities.base_record import BaseRecord
from gv100ad.entities.district import District
from gv100ad.entities.federale_state import FederalState
from gv100ad.entities.government_region import GovernmentRegion
from gv100ad.entities.municipal_association import MunicipalAssociation
from gv100ad.entities.municipality import Municipality
from gv100ad.entities.region import Region

class GV100ADReader:
    """
    A reader for GV100AD files (Gemeindeverzeichnis) provided by Destatis. 
    GV100AD files are UTF-8 encoded.
    """
    
    def __init__(self, text_reader):
        """
        Initializes a new instance of the GV100ADReader class for the specified stream.

        Args:
            text_reader (TextIO): The stream to be read. 
        """
        self._text_reader = text_reader

    def read(self) -> Iterable[BaseRecord]:
        """
        Iterates over the internal GV100AD stream and returns GV100AD records.

        Returns:
            An iterator of BaseRecord-based instances.        
        """
        while True:
            line = self._text_reader.readline()
            if not line:
                break
            yield self._create_record(line.strip())

    async def read_async(self) -> AsyncIterator[BaseRecord]:
        """
        Asynchronously iterates over the internal GV100AD stream and returns GV100AD records.

        Returns:
            An async iterator of BaseRecord-based instances.
        """
        while True:
            line = await self._text_reader.readline()
            if not line:
                break
            yield self._create_record(line.strip())

    def _create_record(self, line) -> BaseRecord:
        """
        Creates the appropriate BaseRecord-based instance by parsing the first 2 characters (Satzart)
        of the given text line.

        Args:
            line (str): The text line to be parsed.

        Returns:
            A new BaseRecord-based instance.
        """
        if line.startswith('10'):
            return FederalState(line)
        elif line.startswith('20'):
            return GovernmentRegion(line)
        elif line.startswith('30'):
            return Region(line)
        elif line.startswith('40'):
            return District(line)
        elif line.startswith('50'):
            return MunicipalAssociation(line)
        elif line.startswith('60'):
            return Municipality(line)
        else:
            raise ValueError(f"Record type {line[:2]} is not supported.")
