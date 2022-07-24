#!/usr/bin/env python3

import subprocess


class SpoofedSignalTransmitter():

    def transmit():
        """
        """
        try:
            #progress = log.progress(log_str)
            subprocess.run(["hackrf_transfer", "-t", "gpssim.bin", "-f", "1575420000"
                , "-s", "2600000", "-a", "1", "-x", "0", "-R"]
                , capture_output=False)
        except Exception as e:
            #progress.failure(e.traceback.format_exc())
            print("\nError during the spoofed signal transmission :\n"+format(e)+"\n\n")
            return 1

        return 0

def main():
    """
    """
    SpoofedSignalTransmitter.transmit()
    return 0

if __name__ == "__main__":
    main()