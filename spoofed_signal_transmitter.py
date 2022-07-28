#!/usr/bin/env python3

import argparse
from ntpath import realpath
import subprocess


BIN_FILE = "gpssim.bin"
FREQ = "1575420000"
SAMPLE_RATE = "2600000"
ENABLE_AMPL = "1"
GAIN = "0"

class SpoofedSignalTransmitter(object):

    def __init__(self, bin_file=BIN_FILE, freq=FREQ
        , sample_rate=SAMPLE_RATE, enable_ampl=ENABLE_AMPL
        , gain=GAIN, repeat=False):
        """
        """
        self.bin_file = bin_file
        self.freq = freq
        self.sample_rate = sample_rate
        self.enable_ampl = enable_ampl
        self.gain = gain
        self.repeat = repeat



    def transmit(self):
        """
        """
        try:
            #progress = log.progress(log_str)
            subprocess.run(["hackrf_transfer", "-t", self.bin_file
                , "-f", self.freq, "-s", self.sample_rate
                , "-a", self.enable_ampl, "-x", self.gain, self.repeat]
                , capture_output=False)
        except Exception as e:
            #progress.failure(e.traceback.format_exc())
            print("\nError during the spoofed signal transmission :\n"+format(e)+"\n\n")
            return 1


def get_parser() -> argparse.ArgumentParser:
    """
    """       
    parser = argparse.ArgumentParser(
        add_help=True, description="Transmit the spoofed GPS signal.")

    parser.add_argument("-t", dest="bin_file", default=BIN_FILE
        , help="The binary file generated from the last retrieved"\
        " GNSS data file.")
    parser.add_argument("-f", dest="freq", default=FREQ
        , help="The frequency of the GPS signal.")
    parser.add_argument("-s", dest="sample_rate", default=SAMPLE_RATE
        , help="Sample frequency (Hz)")
    parser.add_argument("-a", dest="enable_ampl", default=ENABLE_AMPL
        , help="Enable amplification (0 or 1)")
    parser.add_argument("-x", dest="gain", default=GAIN
        , help="Gain (dB)")
    parser.add_argument(
        "-R", action='store_const', const="-R", default=""
        , help="Send the signal repeatedly.")

    return parser


def main() ->int:
    """
    """
    args = get_parser().parse_args()

    transmitter = SpoofedSignalTransmitter(bin_file=args.bin_file
        , freq=args.freq, sample_rate=args.sample_rate
        , enable_ampl=args.enable_ampl, gain=args.gain
        , repeat=args.R) 
    transmitter.transmit()

    return 0

if __name__ == "__main__":
    main()