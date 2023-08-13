import os
import pytest

from incstorage.filesystem import FileSystem
from incstorage.incstorage import Storage


def test_temp_path(temp_path: str):
    """Check that temporal path is a valid path."""
    assert temp_path.startswith('/tmp')
    assert not os.path.exists(temp_path)


def test_temp_workspace(temp_workspace: str):
    """Check that temporal workspace folder is a valid path."""
    assert temp_workspace.startswith('/tmp')
    assert os.path.isdir(temp_workspace)


def test_filesystem(temp_filesystem):
    """Test a file-system creation."""
    assert isinstance(temp_filesystem.path, str)


def test_storage(temp_storage):
    """Test a file-system creation."""
    assert isinstance(temp_storage, Storage)
