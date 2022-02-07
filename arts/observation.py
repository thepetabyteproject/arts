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
