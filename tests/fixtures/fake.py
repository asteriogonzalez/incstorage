"""Generate Fake random Data
"""
import math
import random
import time


from functools import partial
from typing import Union
from faker import Faker
from faker.providers import barcode

fake = Faker()

bc = barcode.Provider(fake)


class Provider:
    """Base Fake Data provider."""

    def __init__(self):
        self.fake = Faker()

    def clock(self, start: Union[float | None] = None, step: int = 2):
        """Create a random regular clock."""
        if start is None:
            start = time.time()

        start = int(start)

        def gen():
            nonlocal start
            start += step
            return start

        return gen

    def rwave(self, a=15, b=45, step=0.1):
        """Create a random sine wave"""
        x = 0
        temp = a
        y0 = (a + b) / 2
        delta = (b - a) / 2

        def gen():
            nonlocal temp, x
            wave = y0 + math.sin(x) * delta
            d = wave - temp
            temp += random.random() * d
            x += step
            return temp

        return gen

    def signal(self, a=0, b=1):
        """Create a random bounded signal."""
        delta = b - a

        def gen():
            return delta * random.random() + a

        return gen

    def isignal(self, a=0, b=100):  # pylint: disable=C0401
        """Create a integer random bounded signal."""
        a, b = int(a), int(b)
        gen = partial(random.randint, a, b)
        return gen


class Sensor(Provider):
    """A Fake Sensor."""

    def __init__(self):
        super().__init__()
        self.data = {}
        self.data['code'] = partial(bc.ean13)
        self.data['signal'] = self.signal()
        self.data['n'] = self.isignal()
        self.data['clock'] = self.clock()
        self.data['temp'] = self.rwave()

    def sample(self):
        """Generate a complete data sample."""
        data = {key: func() for key, func in self.data.items()}
        return data
