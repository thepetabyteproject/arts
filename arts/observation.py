import pygedm
from astropy import units as u
from astropy.coordinates import SkyCoord

from arts.telescope import Telescope


class Observation(Telescope):
    """
    Class for observation properties and calculations.

    """

    def __init__(self):
        self.center_freq = None
        self.bandwidth = None
        self.nchans = None
        self.tsamp = None
        Telescope.__init__(self)

    def chan_freqs(self):
        """

        Returns:

        """
        return 0

    def min_flux(self):
        """

        Returns:

        """
        return 0

    def dm_delay(self, dm):
        """

        Args:
            dm:

        Returns:

        """
        return 0

    def dm_smear_intrachan(self):
        """

        Returns:

        """
        return 0

    def beamsize(self):
        """

        Returns:

        """
        return 0

    def dm_to_dist(self, ra, dec, dm, model):
        """
        
        Args:
            ra (string): right ascension of source
            dec (string): declination of source
            dm (float): dispersion measure (pc/cm^3)
            model (string): electron density model; options are ne2001 and ymw16
        
        Returns:
            dist (float): calculated distance to the source

        """
        coords = SkyCoord(ra, dec, frame='icrs')
        coords = coords.galactic
        l, b = coords.l, coords.b
        # convert to galac
    
        dist, tau_sc = pygedm.dm_to_dist(l, b, dm, method=model)
        
        return dist
    
