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
    myobs = Observation()
    setattr(myobs, "bandwidth", 100)
    setattr(myobs, "center_freq", 350)
    setattr(myobs, "nchans", 512)

    in_strs = ["bw", "lochan", "hichan"]
    # Check that delay = 0 when DM = 0
    for instr in in_strs:
        assert pytest.approx(myobs.dm_delay(0, instr), rel=1e-6) == 0.0

    # Check math for known calculation
    assert pytest.approx(myobs.dm_delay(20), rel=1e-3) == 403.356333333334
    assert pytest.approx(myobs.dm_delay(20, "lochan"), rel=1e-3) == 1.19929396522448
    assert pytest.approx(myobs.dm_delay(20, "hichan"), rel=1e-3) == 0.50681746304299

    # Check that delay = 0 when bandwidth = 0
    setattr(myobs, "bandwidth", 0)
    for instr in in_strs:
        assert pytest.approx(myobs.dm_delay(50, instr), rel=1e-6) == 0.0

    # Check that error is raised when invalid string is passed
    with pytest.raises(ValueError):
        myobs.dm_delay(20, "abcdef")


def test_dm_to_dist():
    obs = Observation()

    assert obs.dm_to_dist("00h00m00s", "00d00m00s", 0, "ne2001").value == 0
    assert obs.dm_to_dist("00h00m00s", "00d00m00s", 0, "ymw16").value == 0

    assert (
        pytest.approx(obs.dm_to_dist("17h45m40s", "-29d00m28s", 10, "ne2001").value, rel=1e-6)
        == 422.4824905395508
    )
    assert (
        pytest.approx(obs.dm_to_dist("17h45m40s", "-29d00m28s", 10, "ymw16").value, rel=1e-6)
        == 517.3521728515625
    )
