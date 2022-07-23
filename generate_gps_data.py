#!/usr/bin/env python3

def retrieve_gnss_file():
    DATE=$(date +"%Y/%m/%d,H:%M:%S")
    YEAR=$(date +"%Y")
    DAY_OF_YEAR=$(date +"%j")
    YEAR_2_LAST_DIGITS=$(date +"%y")

    TMP_GPS_FILE="brdc""$DAY_OF_YEAR""0.""$YEAR_2_LAST_DIGITS""n"    
    FINAL_GPS_FILE="gps_data.n"

    EMAIL="tyreks@hotmail.fr"

    URL="ftps://gdc.cddis.eosdis.nasa.gov/gnss/data/daily/""$YEAR""/""$DAY_OF_YEAR""/""$YEAR_2_LAST_DIGITS""n/""$TMP_GPS_FILE"".gz"

    # latest gps data file retrieving from NASA site
    wget --ftp-user anonymous --ftp-password $EMAIL $URL &&\

    # temporary gps data file extracting
    gunzip -f $TMP_GPS_FILE".gz"
    mv $TMP_GPS_FILE $FINAL_GPS_FILE

    return 0

def generate_gps_data():
    return 0

def spoof_gps():
    return 0


def main():
    retrieve_gnss_file()
    generate_gps_data()
    spoof_gps()
    return 0

if __name__ == "__main__":
    main()