"""Test basic features of Storage
"""

from incstorage.filesystem import FileSystem
from incstorage.incstorage import Record, Storage


def test_format_record():
    """Check that record can be serialized."""


def test_new_chunk_creation():
    """Check when a record forces the creation of a new chunk."""


def test_monotonic_keys():
    """Check that the given generated key algorithm creates a
    monotonic key series.
    """


def test_key_in_the_past():
    """Check error handling when we found a key in the 'past'"""


def test_record_can_not_be_formatted():
    """Check error handling when a record failed to be formatted."""


def test_clean_old_data():
    """Check cleaning 'old' data."""


# --------------------------------------
# test populate storage
# --------------------------------------
def test_populate_storage(temp_storage):
    """Test that storage can store simple random data."""
    assert isinstance(temp_storage, Storage)
