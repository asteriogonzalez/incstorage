"""This module will test Virtual File System Implementation over
physical storage.

- [ ] record serialization into CSV format.
- [ ] chunk definition.

"""

from incstorage.filesystem import FileSystem


def test_uc01_record_serialization(temp_filesystem):
    """TBD"""
    fs = temp_filesystem
    assert isinstance(fs, FileSystem)
    foo = 1


def test_uc01_virtual_fs(temp_filesystem):
    """TBD"""
    fs = temp_filesystem
    assert isinstance(fs, FileSystem)
    foo = 1
