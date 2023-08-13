"""
TODO:

- [ ] random record generation
- [ ]

"""
import pytest


from incstorage.incstorage import Storage
from incstorage.filesystem import FileSystem


@pytest.fixture
def temp_filesystem(temp_workspace):
    """Return a virtual fs."""
    url = f'file:///{temp_workspace}'
    fs = FileSystem(url=url)
    yield fs


@pytest.fixture
def temp_storage(temp_filesystem):
    """Return a storage to any test case."""

    st = Storage(fs=temp_filesystem)
    yield st
