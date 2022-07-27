#!/usr/bin/env python3

# parseur des arguments de la commande
import argparse

from requests import get
import gnss_data_retriever as gdr
import gps_data_generator as gdg
import spoofed_signal_transmitter as sst


def get_parser() -> argparse.ArgumentParser:
    """
    """
               
    parser = argparse.ArgumentParser(
        add_help=True, description="Retrieve the moste recent daily GNSS data file from the NASA site, generate the associated binary and transmit it to spoof the real GPS signal")

    parser.add_argument(
        "--retrieve", action='store_const', const=True, default=False, help="Retrieve the moste recent daily GNSS data file from the NASA site")

    parser.add_argument(
        "--generate", action='store_const', const=True, default=False, help="Generate the binary GPS data from the local GNSS file.")

    parser.add_argument(
        "--transmit", action='store_const', const=True, default=False, help="Transmit the GPS signal from the local binary GPS data.")

    

    return parser


def main():
    """
    """
    args = get_parser().parse_args()

    if not args.retrieve and not args.generate and not args.transmit: #full process
        gdr.GnssDataRetriever.retrieve_gnss_file()
        gdg.GpsDataGenerator.generate_gps_data()
        sst.SpoofedSignalTransmitter.transmit()

    if args.retrieve:
        gdr.GnssDataRetriever.retrieve_gnss_file()

    if args.generate:
        gdg.GpsDataGenerator.generate_gps_data()
    
    if args.transmit:
        sst.SpoofedSignalTransmitter.transmit()

    return 0

if __name__ == "__main__":
    main()

    # if no argument, launch full process
    # if arg == -l afa,fafa,fafa => option -l de gps-sdr-sim
    # if arg == -L file => cat file

    # if arg == --generate => generate
    # if arg == --transmit =>
    # if arg == --retrieve =>  