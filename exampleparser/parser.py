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

"""
class HDF5Parser():

    def parse(self, mainfile: str, archive: EntryArchive, logger):
        reader = HDF5Reader(mainfile)
        data = reader.extract_metadata()

        # Example: store something in archive
        section = HDF5Metadata()
        section.method = 'HDF5 metadata extraction'
        section.comments = str(data.get('some_group', {}).get('value', 'No value'))

        archive.metadata.entry_name = 'HDF5 extracted entry'
        archive.run = [section]

"""

from nomad.datamodel import EntryArchive, EntryMetadata

class HDF5Parser():
    def parse(self, mainfile: str, archive: EntryArchive, logger):
        from .hdf5_parser import HDF5Reader
        from .metainfo.example import HDF5Metadata

        reader = HDF5Reader(mainfile)
        data = reader.extract_metadata()

        section = HDF5Metadata()
        section.file_structure = str(data)
        section.temperature = float(
            data.get('experiment', {}).get('temperature', {}).get('value', 0.0)
        )

        # ✅ Initialize metadata if needed
        if archive.metadata is None:
            from nomad.datamodel import EntryMetadata
            archive.metadata = EntryMetadata()

        archive.metadata.entry_name = 'HDF5 extracted entry'
        archive.results = section


"""
class ExampleParser:
    def parse(self, mainfile: str, archive: EntryArchive, logger):
        # Log a hello world, just to get us started. TODO remove from an actual parser.
        logger.info('Hello World')

        # Use the previously defined parsers on the given mainfile
        mainfile_parser.mainfile = mainfile
        mainfile_parser.parse()

        simulation = Simulation(
            code_name='super_code', code_version=mainfile_parser.get('program_version')
        )
        date = datetime.datetime.strptime(mainfile_parser.date, '%Y/%m/%d')
        simulation.date = date

        for calculation in mainfile_parser.get('calculation', []):
            model = Model()

            model.lattice = calculation.get('lattice_vectors')
            sites = calculation.get('sites')
            model.labels = [site[0] for site in sites]
            model.positions = [site[1] for site in sites]
            simulation.model.append(model)

            output = Output()
            output.model = model
            output.energy = calculation.get('energy') * units.eV
            magic_source = calculation.get('magic_source')
            if magic_source is not None:
                archive.workflow2 = Workflow(x_example_magic_value=magic_source)
            simulation.output.append(output)
        # put the simulation section into archive data
        archive.data = simulation

"""