#!/usr/bin/env python3

#!/bin/bash

# args number verification



import datetime
from logging import error
import subprocess

GPS_SDR_SIM = "../gps-sdr-sim/gps-sdr-sim"
INPUT_EPHEM_FILE="gps_data.n"
SAMPLE_FREQ="2600000"
DATE=datetime.datetime.today().strftime("%Y/%m/%d,07:%M:%S")
BITS="8"
LOCATION="35.504452495375716,11.057292641491118,100"
DURATION = "30"
#LOCATION=`cat $1`

class GpsDataGenerator:
    def generate_gps_data(date=DATE, input_ephem_file=INPUT_EPHEM_FILE
        ,bits=BITS, sample_freq=SAMPLE_FREQ, location=LOCATION, duration=DURATION):
        try:
            #progress = log.progress(log_str)
            subprocess.run([GPS_SDR_SIM, "-t", date, "-e", input_ephem_file
                , "-b", bits, "-s", sample_freq, "-l", location, "-d", duration]
                , capture_output=False)
        except Exception as e:
            #progress.failure(e.traceback.format_exc())
            print("\nError during GPS data generation :\n"+format(e)+"\n\n")
            return 1
        #progress.success()
        return 0

def main():
    GpsDataGenerator.generate_gps_data()
    return 0

if __name__ == "__main__":
    main()
