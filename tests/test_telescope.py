import numpy as np

from arts.telescope import Telescope


def test_telescope():
    tel = Telescope()
    tel.dishsize = 30
    tel.location = np.zeros((3, 1))

    assert tel.dishsize == 30
    assert tel.ndishes == 1
