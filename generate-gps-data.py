#!/usr/bin/env python3

#!/bin/bash

# args number verification



import datetime
from logging import error
import subprocess

GPS_SDR_SIM = "../../sdr/gps-sdr-sim/gps-sdr-sim"
INPUT_EPHEM_FILE="gps_data.n"
SAMPLE_FREQ="2600000"
DATE=datetime.datetime.today().strftime("%Y/%m/%d,07:%M:%S")
BITS="8"
LOCATION="35.504452495375716,11.057292641491118,100"
DURATION = "30"
#LOCATION=`cat $1`


def generate_gps_data():
    try:
        #progress = log.progress(log_str)
        subprocess.run([GPS_SDR_SIM, "-t", DATE, "-e", INPUT_EPHEM_FILE
            , "-b", BITS, "-s", SAMPLE_FREQ, "-l", LOCATION, "-d", DURATION, "-t", DATE]
            , capture_output=False)
    except Exception as e:
        #progress.failure(e.traceback.format_exc())
        print("\nError during GPS data generation :\n"+format(e)+"\n\n")
        return 1
    #progress.success()
    return 0

def main():
    generate_gps_data()
    return 0

if __name__ == "__main__":
    main()
