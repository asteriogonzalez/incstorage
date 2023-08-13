import os
import random
import time
import shutil

import pytest


def _temp_path(prefix="", sufix=""):
    return f"/tmp/{prefix}{time.time()}.{random.randint(0, 10**9)}{sufix}"


@pytest.fixture()
def temp_path(prefix="", sufix=""):
    """Returns a random path."""
    return _temp_path(prefix, sufix)


@pytest.fixture()
def temp_workspace(prefix="", sufix=""):
    """Create a temporal folder that all content will be removed
    at the end of the test.
    """
    root = _temp_path(prefix, sufix)
    os.makedirs(root, exist_ok=True)
    yield root

    shutil.rmtree(root)
