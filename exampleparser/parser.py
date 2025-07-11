#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import datetime

import numpy as np
from nomad.datamodel import EntryArchive
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.file_parser import Quantity, TextParser
from nomad.units import ureg as units


"""
This is a hello world style example for an example parser/converter.
"""


from nomad.datamodel import EntryArchive
from .metainfo.example import HDF5Metadata
from .hdf5_parser import HDF5Reader
from nomad.parsing.parser import Parser

class HDF5Parser(Parser):
    def __init__(self):
        super().__init__(
            name='parser_hdf5',
            code_name='HDF5 Example Parser',
            code_homepage='https://example.org/hdf5parser',
            domain='data',
        )

    def parse(self, mainfile: str, archive: EntryArchive, logger):
        reader = HDF5Reader(mainfile)
        data = reader.extract_metadata()

        # Example: store something in archive
        section = HDF5Metadata()
        section.method = 'HDF5 metadata extraction'
        section.comments = str(data.get('some_group', {}).get('value', 'No value'))

        archive.metadata.entry_name = 'HDF5 extracted entry'
        archive.run = [section]