import numpy as np


class Telescope:
    """
    Class with Telescope properties.

    """

    def __init__(
        self, name=None, location=np.array([]), dishsize=None, tsys=None, gain=None
    ):
        self.name = name
        self.location = location
        self.dishsize = dishsize
        self.tsys = tsys
        self.gain = gain

    @property
    def ndishes(self):
        """

        Returns:

        """
        return self.location.shape[1]
