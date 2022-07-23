#!/usr/bin/env python3

#!/bin/bash

# args number verification



import datetime
from logging import error
import subprocess


GPS_SDR_SIM = "../sdr/gps-sdr-sim/gps-sdr-sim"
TMP_ZIP="tmp_zip.gz"
INPUT_EPHEM_FILE="gps_data.n"
SAMPLE_FREQ=2600000
DATE=datetime.today().strftime("%Y/%m/%d,H:%M:%S")
BITS=8
#LOCATION="48.826907303230875,2.3664011786965418,100"
#LOCATION="48.90077718505967,2.358593792356755,100"
LOCATION="35.504452495375716,11.057292641491118,100"
#LOCATION=`cat $1`

# stream data generating
#$GPS_SDR_SIM -t $DATE -e $INPUT_EPHEM_FILE -b $BITS -s $SAMPLE_FREQ -l $LOCATION






def generate_gps_data():
    try:
        #progress = log.progress(log_str)
        subprocess.run([GPS_SDR_SIM, "-t", DATE, "-e", INPUT_EPHEM_FILE
            , "-b", BITS, "-s", SAMPLE_FREQ, "-l", LOCATION], capture_output=False)
    except Exception as e:
        #progress.failure(e.traceback.format_exc())
        print("Error during GPS data generation")
        return 1
    #progress.success()
    return 0

def main():
    generate_gps_data()
    return 0

if __name__ == "__main__":
    main()