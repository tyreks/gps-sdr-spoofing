#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import datetime
import gzip
import shutil
from ftplib import FTP_TLS
from configparser import ConfigParser
import sys


class GnssDataRetriever(object) :
    
    # remote NASA host
    host : str

    def __init__(self, host=None, mail=None) -> None:
        """
        """
        parser = ConfigParser()
        parser.read("config_gps_spoofer.ini")
        self.host = host if host != None else parser["RETRIEVER"]["HOST"]
        self.mail = mail if mail != None else parser["RETRIEVER"]["MAIL"]


    def retrieve_gnss_file(self):
        """
        retrieve the most recent GNSS daily file from the NASA site
        """
 
        # remote NASA host

        # date retrieving
        TODAY = datetime.datetime.today()
        YEAR = TODAY.strftime("%Y")
        DAY_OF_YEAR = TODAY.strftime("%j")
        YEAR_2_LAST_DIGITS = TODAY.strftime("%y")

        # temporary and final result files names
        TMP_GPS_FILE="brdc"+DAY_OF_YEAR+"0."+YEAR_2_LAST_DIGITS+"n.gz"    
        FINAL_GPS_FILE="gps_data.n"

        # email, used as a password for the ftps download
        EMAIL="tyreks@hotmail.fr"

     
        # ftp remote directory
        DIRECTORY = "gnss/data/daily/"+YEAR+"/"+DAY_OF_YEAR+"/"+YEAR_2_LAST_DIGITS+"n/"

        # latest gps data file retrieving from NASA site
        ftps = FTP_TLS(host = self.host)
        ftps.login(user="anonymous", passwd=EMAIL)
        ftps.prot_p()
        ftps.cwd(DIRECTORY)
        ftps.retrbinary("RETR " + TMP_GPS_FILE, open(TMP_GPS_FILE, "wb").write)

        # temporary file extracting and renaming to final file
        with gzip.open(TMP_GPS_FILE, "rb") as f_in:
            with open(FINAL_GPS_FILE, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        # remove the temporary file
        if os.path.exists(TMP_GPS_FILE):
            os.remove(TMP_GPS_FILE)

        return 0


def main():
    try:
        retriever = GnssDataRetriever()
        retriever.retrieve_gnss_file()
    except Exception as exc:
        print (format(exc))
        sys.exit(1)
    return 0

if __name__ == "__main__":
    main()