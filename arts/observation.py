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
            dm (float): dispersion measure (pc/cm^3)

        Returns: 
            t_delay_bw (float): dispersion delay across bandwidth in ms
            t_delay_lowchan (float): dispersion delay across lowest frequency channel in ms
            t_delay_hichan (float): dispersion delay across highest frequency channel in ms

        """
        hf = self.center_freq + (self.bandwidth/2.)
        lf = self.center_freq - (self.bandwidth/2.)
        #Make sure frequencies are in MHz otherwise this is wrong

        chan_width = self.bandwidth/self.nchans
        lowchan_end = lf + chan_width #upper frequency of lowest-frequency channel
        hichan_start = hf - chan_width #lower frequency of highest-frequency channel

        t_delay_bw = 4148808 * dm * ( (lf**(-2)) - (hf**(-2)) ) #delay across BW in ms
        t_delay_lowchan = 4148808 * dm * ( (lf**(-2)) - (lowchan_end**(-2)) ) #delay across lowest channel in ms
        t_delay_hichan = 4148808 * dm * ( (hichan_start**(-2)) - (hf**(-2)) ) #delay across highest channel in ms
        return t_delay_bw, t_delay_lowchan, t_delay_hichan

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
