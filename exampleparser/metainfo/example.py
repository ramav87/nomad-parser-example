from nomad.metainfo import Package, Section, Quantity
from nomad.datamodel.metainfo.basesections import ArchiveSection 

m_package = Package(name='hdf5parser_metadata')

class HDF5Metadata(ArchiveSection):

    description = 'Metadata extracted from an HDF5 file'
    m_def = Section(
        label='HDF5 metadata',
        description='Metadata extracted from HDF5 files.'
    )

    file_structure = Quantity(
        type=str,
        description='String representation of the HDF5 file structure'
    )

    temperature = Quantity(
        type=float,
        unit='kelvin',
        description='Example temperature extracted from HDF5'
    )

m_package.__init_metainfo__()
