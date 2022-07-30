#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from configparser import ConfigParser
import datetime
import subprocess


#LOCATION="35.504452495375716,11.057292641491118,100"

class GpsDataGenerator(object):

    def __init__(self, date=None, input_ephem_file=None
        ,bits=None, sample_rate=None, location=None, duration=None):
        """
        """
        parser = ConfigParser()
        parser.read("config_gps_spoofer.ini")

        self.input_ephem_file = input_ephem_file \
            if input_ephem_file != None \
            else parser["GENERATOR"]["INPUT_EPHEM_FILE"]

        self.bits = bits if bits != None \
            else parser["GENERATOR"]["BITS"]

        self.sample_rate = sample_rate if sample_rate != None \
            else parser["GENERATOR"]["SAMPLE_RATE"]
            
        self.duration = duration if duration != None \
            else parser["GENERATOR"]["DURATION"]

        self.date = date if date != None\
            else datetime.datetime.today().strftime("%Y/%m/%d,07:%M:%S")

        self.location = location

        self.gps_sdr_sim = parser["GENERATOR"]["GPS_SDR_SIM"]


    def generate_gps_data(self):
        """
        """
        try:
            subprocess.run([self.gps_sdr_sim, "-t", self.date, "-e"
                , self.input_ephem_file, "-b", self.bits, "-s"
                , self.sample_rate, "-l", self.location, "-d"
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

    parser.add_argument("-l", dest="location", required=True
        , help="GPS location to transmit.")

    parser.add_argument("-t", dest="date"
        , help="date (YYYY/MM/DD,HH:MM:SS).")

    parser.add_argument("-e", dest="input_ephem_file"
        , help="GNSS ephemeris file.")

    parser.add_argument("-b", dest="bits"
        , help="Number of bits.")

    parser.add_argument("-s", dest="sample_rate"
        , help="Sample rate (Hz).")

    parser.add_argument("-d", dest="duration"
        , help="Duration of the signal transmission.")

    return parser


def main():
    """
    """
    args = get_parser().parse_args()

    my_generator = GpsDataGenerator(date=args.date
        , input_ephem_file=args.input_ephem_file, bits=args.bits
        , sample_rate=args.sample_rate, location=args.location
        , duration=args.duration)

    my_generator.generate_gps_data()

    return 0

if __name__ == "__main__":
    main()