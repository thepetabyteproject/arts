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

    def dm_delay(self, dm, t_out="bw"):
        """
        Args:
            dm (float): dispersion measure (pc/cm^3)
            t_out (str): which dispersion delay the function returns.
              Default: "bw" = delay across entire bandwidth
              "hichan" = delay across highest frequency channel
              "lochan" = delay across lowest frequency channel

        Returns:
            t_delay (float): dispersion delay across desired frequency range, in ms

        """

        hf = self.center_freq + (self.bandwidth / 2.0)
        lf = self.center_freq - (self.bandwidth / 2.0)
        # Make sure frequencies are in MHz otherwise this is wrong

        chan_width = self.bandwidth / self.nchans
        lowchan_end = lf + chan_width  # upper frequency of lowest-frequency channel
        hichan_start = hf - chan_width  # lower frequency of highest-frequency channel

        if t_out not in ["bw", "hichan", "lochan"]:
            raise ValueError(
                "Output string should be one of the preset values: 'bw', 'hichan', or 'lochan'"
            )

        if t_out == "bw":
            t_delay = (
                4148808 * dm * ((lf ** (-2)) - (hf ** (-2)))
            )  # delay across BW in ms
        elif t_out == "lowchan":
            t_delay = (
                4148808 * dm * ((lf ** (-2)) - (lowchan_end ** (-2)))
            )  # delay across lowest channel in ms
        elif t_out == "hichan":
            t_delay = (
                4148808 * dm * ((hichan_start ** (-2)) - (hf ** (-2)))
            )  # delay across highest channel in ms

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
