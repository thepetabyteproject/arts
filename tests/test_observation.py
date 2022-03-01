import numpy as np
import pytest
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
        obs.dm_delay(20, "abcdef")
