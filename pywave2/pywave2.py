"""Main entry point"""
import argparse
import os
import sys
from buoydata import get_buoy_data


def main():
    """Entry point function"""

    # first check to see if the user passed env vars
    # if they didn't then try to parse args
    station_id = os.environ.get('PYWAVE_STATIONID') or parse_args().station_id
    if not station_id:
        print('You must define the station id')
        sys.exit(1)

    print(get_buoy_data(station_id))
    sys.exit(0)


def parse_args():
    """Parse command-line arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--station_id',
        help='The station id to pull data from'
    )
    return parser.parse_args()
