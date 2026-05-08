##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

import pytest
import asyncio
from datetime import datetime
from io import StringIO
from gv100ad.entities.district_type import DistrictType
from gv100ad.entities.municipal_association_type import MunicipalAssociationType
from gv100ad.entities.municipality_type import MunicipalityType
from gv100ad.reader import GV100ADReader


class AsyncStringReader:
    def __init__(self, text: str):
        self._lines = iter(text.splitlines(keepends=True))

    async def readline(self):
        return next(self._lines, "")


def test_district():
    text_line = "402022013108221       Heidelberg, Stadtkreis                            Heidelberg                                        42                                                                                                "
    str_stream = StringIO(text_line)

    gv_reader = GV100ADReader(str_stream)
    enumerator = gv_reader.read().__iter__()

    record = enumerator.__next__()
    assert record.timestamp == datetime(2022, 1, 31).date()
    assert record.regional_code == "08221"
    assert record.name == "Heidelberg, Stadtkreis"
    assert record.administrative_headquarters == "Heidelberg"
    assert record.type == DistrictType.STADTKREIS

    with pytest.raises(StopIteration):
        enumerator.__next__()


def test_federal_state():
    text_line = "102022013101          Schleswig-Holstein                                Kiel                                                                                                                                                "
    str_stream = StringIO(text_line)

    gv_reader = GV100ADReader(str_stream)
    enumerator = gv_reader.read().__iter__()

    record = enumerator.__next__()
    assert record.timestamp == datetime(2022, 1, 31).date()
    assert record.regional_code == "01"
    assert record.name == "Schleswig-Holstein"
    assert record.seat_of_government == "Kiel"

    with pytest.raises(StopIteration):
         enumerator.__next__()


def test_government_region():
    text_line = "2020220131051         Reg.-Bez. Düsseldorf                              Düsseldorf                                                                                                                                          "
    str_stream = StringIO(text_line)

    gv_reader = GV100ADReader(str_stream)
    enumerator = gv_reader.read().__iter__()

    record = enumerator.__next__()
    assert record.timestamp == datetime(2022, 1, 31).date()
    assert record.regional_code == "051"
    assert record.name == "Reg.-Bez. Düsseldorf"
    assert record.administrative_headquarters == "Düsseldorf"

    with pytest.raises(StopIteration):
        enumerator.__next__()


def test_municipal_association():
    text_line = "502022013108221   0000Heidelberg, Stadt                                                                                   50                                                                                                "
    str_stream = StringIO(text_line)

    gv_reader = GV100ADReader(str_stream)
    enumerator = gv_reader.read().__iter__()

    record = enumerator.__next__()
    assert record.timestamp == datetime(2022, 1, 31).date()
    assert record.regional_code == "08221"
    assert record.association == "0000"
    assert record.name == "Heidelberg, Stadt"
    assert record.administrative_headquarters == ""
    assert record.type == MunicipalAssociationType.VERBANDSFREIE_GEMEINDE

    with pytest.raises(StopIteration):
        enumerator.__next__()


def test_municipality():
    text_line = "6020220131082260135001Eberbach, Stadt                                                                                     63    000000081150000001426700000006914    69412*****  2840130262405277                           "
    str_stream = StringIO(text_line)

    gv_reader = GV100ADReader(str_stream)
    enumerator = gv_reader.read().__iter__()

    record = enumerator.__next__()
    assert record.timestamp == datetime(2022, 1, 31).date()
    assert record.regional_code == "08226013"
    assert record.association == "5001"
    assert record.name == "Eberbach, Stadt"
    assert record.type == MunicipalityType.STADT
    assert record.postal_code == "69412"
    assert record.multiple_postal_codes is True
    assert record.tax_office_district == "2840"
    assert record.higher_regional_court_district == "1"
    assert record.regional_court_district == "3"
    assert record.local_court_district == "02"
    assert record.employment_agency_district == "62405"

    with pytest.raises(StopIteration):
        enumerator.__next__()


def test_region():
    text_line = "30202201310822        Region Rhein-Neckar                               Mannheim                                                                                                                                            "
    str_stream = StringIO(text_line)

    gv_reader = GV100ADReader(str_stream)
    enumerator = gv_reader.read().__iter__()

    record = enumerator.__next__()
    assert record.timestamp == datetime(2022, 1, 31).date()
    assert record.regional_code == "0822"
    assert record.name == "Region Rhein-Neckar"
    assert record.administrative_headquarters == "Mannheim"

    with pytest.raises(StopIteration):
        enumerator.__next__()


def test_municipality_raises_for_invalid_postal_code_marker():
    text_line = "6020220131082260135001Eberbach, Stadt                                                                                     63    000000081150000001426700000006914abcde  2840130262405277                           "
    gv_reader = GV100ADReader(StringIO(text_line))

    with pytest.raises(ValueError, match="Invalid postal code marker"):
        next(gv_reader.read())


def test_read_async_with_sync_string_reader():
    text_line = "102022013101          Schleswig-Holstein                                Kiel                                                                                                                                                \n"
    gv_reader = GV100ADReader(StringIO(text_line))

    async def collect_records():
        return [record async for record in gv_reader.read_async()]

    records = asyncio.run(collect_records())

    assert len(records) == 1
    assert records[0].regional_code == "01"
    assert records[0].name == "Schleswig-Holstein"


def test_read_async_with_async_reader():
    text_line = "2020220131051         Reg.-Bez. Düsseldorf                              Düsseldorf                                                                                                                                          \n"
    gv_reader = GV100ADReader(AsyncStringReader(text_line))

    async def collect_records():
        return [record async for record in gv_reader.read_async()]

    records = asyncio.run(collect_records())

    assert len(records) == 1
    assert records[0].regional_code == "051"
    assert records[0].administrative_headquarters == "Düsseldorf"


def test_read_skips_blank_lines():
    text = "\n\r\n102022013101          Schleswig-Holstein                                Kiel                                                                                                                                                \n"
    gv_reader = GV100ADReader(StringIO(text))

    records = list(gv_reader.read())

    assert len(records) == 1
    assert records[0].regional_code == "01"
