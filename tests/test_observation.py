import numpy as np

from arts.observation import Observation
from arts.telescope import Telescope


def test_observation():
    tel = Telescope()
    tel.dishsize = 30
    tel.location = np.zeros((3, 1))

    obs = Observation()


def test_min_flux():
    assert 1 == 1


def test_dm_delay():
    assert 1 == 1
