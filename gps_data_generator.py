#!/usr/bin/env python3

import argparse
import datetime
import subprocess


GPS_SDR_SIM = "../gps-sdr-sim/gps-sdr-sim"
INPUT_EPHEM_FILE="gps_data.n"
SAMPLE_FREQ="2600000"
DATE=datetime.datetime.today().strftime("%Y/%m/%d,07:%M:%S")
BITS="8"
LOCATION="35.504452495375716,11.057292641491118,100"
DURATION = "30"

class GpsDataGenerator(object):

    def __init__(self, date=DATE, input_ephem_file=INPUT_EPHEM_FILE
        ,bits=BITS, sample_freq=SAMPLE_FREQ, location=LOCATION, duration=DURATION):
        """
        """
        self.date = date
        self.input_ephem_file = input_ephem_file
        self.bits = bits
        self.sample_freq = sample_freq
        self.location = location
        self.duration = duration


    def generate_gps_data(self):
        """
        """
        print(self.bits)
        try:
            subprocess.run([GPS_SDR_SIM, "-t", self.date, "-e"
                , self.input_ephem_file, "-b", self.bits, "-s"
                , self.sample_freq, "-l", self.location, "-d"
                , self.duration], capture_output=False)
        except Exception as e:
            print("\nError during GPS data generation :\n"+format(e)+"\n\n")
            return 1
        return 0


def get_parser() -> argparse.ArgumentParser:
    """
    """       
    parser = argparse.ArgumentParser(
        add_help=True, description="Generate the associated"\
            " binary from the local GNSS data file.")
    
    parser.add_argument("-t", dest="date", default=DATE
        , help="date (YYYY/MM/DD,HH:MM:SS)")
    parser.add_argument("-e", dest="input_ephem_file"
        , default=INPUT_EPHEM_FILE
        , help="GNSS ephemeris file")
    parser.add_argument("-b", dest="bits", default=BITS
        , help="Number of bits")
    parser.add_argument("-s", dest="sample_freq", default=SAMPLE_FREQ
        , help="Sample frequency (Hz)")
    parser.add_argument("-l", dest="location", default=LOCATION
        , help="Location")
    parser.add_argument("-d", dest="duration", default=DURATION
        , help="Duration (s)")

    return parser


def main():
    """
    """
    args = get_parser().parse_args()

    my_generator = GpsDataGenerator(date=args.date
        , input_ephem_file=args.input_ephem_file, bits=args.bits
        , sample_freq=args.sample_freq, location=args.location
        , duration=args.duration)

    my_generator.generate_gps_data()

    return 0

if __name__ == "__main__":
    main()