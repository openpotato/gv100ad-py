##
# Copyright (c) STÜBER SYSTEMS GmbH
# Licensed under the MIT License, Version 2.0. 
##

from datetime import datetime

class BaseRecord:
    def __init__(self, line):
        """
        Initializes a new instance of the BaseRecord class.

        Args:
            line (str): A text row from a GV100AD file.
        """
        self.timestamp = datetime.strptime(line[2:10], "%Y%m%d").date()
        self.name = line[22:72].rstrip()

    def __repr__(self):
        return f"BaseRecord(Name={self.name}, TimeStamp={self.timestamp})"
