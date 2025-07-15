import h5py
from typing import Any, Dict

class HDF5Reader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_metadata(self, group_path: str = '/') -> Dict[str, Any]:
        """Recursively extract metadata and datasets from the HDF5 file."""
        metadata = {}

        def _walk(obj, out):
            if isinstance(obj, h5py.Group):
                for key, item in obj.items():
                    out[key] = {}
                    _walk(item, out[key])
            elif isinstance(obj, h5py.Dataset):
                out['value'] = obj[()]              
                out['attrs'] = dict(obj.attrs)      

        with h5py.File(self.file_path, 'r') as f:
            _walk(f[group_path], metadata)
        return metadata
