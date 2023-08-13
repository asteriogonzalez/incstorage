"""Helpers shared by mockup and real test implementations.
"""
import random
import time

from datetime import datetime

# ----------------------------------------------------------
# External helpers
# ----------------------------------------------------------

from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()

# ----------------------------------------------------------
# monotonic counter
# ----------------------------------------------------------
global_counter = 0


def next_uid():
    """Provides a global monotonic counter, normally used as
    unique-integer indentifier
    """

    global global_counter
    global_counter += 1
    return global_counter


# ----------------------------------------------------------
# Fake year provider
# ----------------------------------------------------------

year_provider = DynamicProvider(
    provider_name="year",
    elements=list(range(2018, datetime.now().year + 1)),
)

fake.add_provider(year_provider)


# ----------------------------------------------------------
# TODO: External Audit
# ----------------------------------------------------------
def null(*args, **kw):
    "a helper 'do-nothing' function"


# console = print
console = null
