#!/usr/bin/env python3

import argparse
import gnss_data_retriever as gdr
import gps_data_generator as gdg
import spoofed_signal_transmitter as sst


class SmeetaGpsSpoofer(object):

    def __init__(self, retrieve=False, generate=False
        , transmit=False):
        """
        """
        self.retrieve = retrieve
        self.generate = generate
        self.transmit = transmit


    def spoof(self):
        """
        """
        if not (self.retrieve or self.generate or self.transmit):
            retriever = gdr.GnssDataRetriever()
            generator = gdg.GpsDataGenerator()
            transmitter = ""#sst

            #retriever.retrieve_gnss_file()
            generator.generate_gps_data()
            #transmitter.transmit()

        else :
            if self.retrieve:
                retriever = gdr.GnssDataRetriever()
                retriever.retrieve_gnss_file()

            if self.generate:
                generator = gdg.GpsDataGenerator()
                generator.generate_gps_data()
            
            if self.transmit:
                transmitter = ""#sst.SpoofedSignalTransmitter()
                #transmitter.transmit()



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
    return parser


def main() -> int:
    """
    """
    args = get_parser().parse_args()

    spoofer = SmeetaGpsSpoofer(args.retrieve, args.generate
        , args.transmit)

    spoofer.spoof()

    return 0

if __name__ == "__main__":
    main() 