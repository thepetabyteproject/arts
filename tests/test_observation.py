import numpy as np
import pygedm
import pytest
from astropy import units as u
from astropy.coordinates import SkyCoord

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


def test_dm_to_dist():
    obs = Observation()

    assert obs.dm_to_dist("00h00m00s", "00d00m00s", 0, "ne2001") == 0
    assert obs.dm_to_dist("00h00m00s", "00d00m00s", 0, "ymw16") == 0

    assert (
        pytest.approx(obs.dm_to_dist("17h45m40s", "-29d00m28s", 10, "ne2001").value, rel=1e-6)
        == 422.4824905395508
    )
    assert (
        pytest.approx(obs.dm_to_dist("17h45m40s", "-29d00m28s", 10, "ymw16").value, rel=1e-6)
        == 517.3521728515625
    )
