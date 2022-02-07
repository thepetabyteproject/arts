import numpy as np


class Telescope:
    """
    Class with Telescope properties.

    """

    def __init__(self):
        self.name = None
        self.location = np.array([])
        self.dishsize = None
        self.tsys = None
        self.gain = None

    @property
    def ndishes(self):
        """

        Returns:

        """
        return self.location.shape[1]
