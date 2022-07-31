#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import gnss_data_retriever as gdr
import gps_data_generator as gdg
import spoofed_signal_transmitter as sst


class SmeetaGpsSpoofer(object):

    def __init__(self, retrieve=False, generate=False
        , transmit=False, location=None):
        """
        """
        self.retrieve = retrieve
        self.generate = generate
        self.transmit = transmit
        self.location = location


    def spoof(self):
        """
        """
        try:
            if not (self.retrieve or self.generate or self.transmit):

                if (self.location == None):
                    raise Exception ("Required argument : -l LOCATION \n"\
                    "It has to be specified for the full gps spoofing processing")

                retriever = gdr.GnssDataRetriever()
                generator = gdg.GpsDataGenerator()
                transmitter = sst.SpoofedSignalTransmitter()

                retriever.retrieve_gnss_file()
                generator.generate_gps_data()
                transmitter.transmit()

            else :
                if self.retrieve:
                    retriever = gdr.GnssDataRetriever()
                    retriever.retrieve_gnss_file()

                if self.generate:
                    if (self.location == None):
                        raise Exception ("Required argument : -l LOCATION \n"\
                        "It has to be specified for the gps data file generation")
                    generator = gdg.GpsDataGenerator()
                    generator.generate_gps_data()
                
                if self.transmit:
                    transmitter = sst.SpoofedSignalTransmitter()
                    transmitter.transmit()
        except Exception as exc:
            print (format(exc))
            sys.exit(1)



def get_parser() -> argparse.ArgumentParser:
    """
    """       
    parser = argparse.ArgumentParser(
        add_help=True, description="Retrieve the moste recent daily"\
            " GNSS data file from the NASA site, generate the associated"\
            " binary and transmit it to spoof the real GPS signal.")

    parser.add_argument(
        "--retrieve", action='store_const', const=True, default=False
        , help="Retrieve the most recent daily GNSS data file from the NASA site.")

    parser.add_argument(
        "--generate", action='store_const', const=True, default=False
        , help="Generate the binary GPS data from the local GNSS file.")

    parser.add_argument(
        "--transmit", action='store_const', const=True, default=False
        , help="Transmit the GPS signal from the local binary GPS data.")

    parser.add_argument("-l", dest="location"
        , help="GPS location to transmit.")

    return parser


def main() -> int:
    """
    """
    args = get_parser().parse_args()

    spoofer = SmeetaGpsSpoofer(args.retrieve, args.generate
        , args.transmit, args.location)

    spoofer.spoof()

    return 0

if __name__ == "__main__":
    main() 