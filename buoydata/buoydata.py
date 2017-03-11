"""BuoyData class"""
import re
from bs4 import BeautifulSoup
import requests


# pylint: disable=too-few-public-methods
class BuoyData:
    """Buoy data storage class"""

    def __init__(self, station_id, swell_height, swell_period, swell_direction):
        self.station_id = station_id
        self.swell_height = swell_height
        self.swell_period = swell_period
        self.swell_direction = swell_direction

    def __str__(self):
        return '{}@{} sec {}'.format(
            self.swell_height,
            self.swell_period,
            self.swell_direction)


def get_buoy_data(station_id):
    """Get and parse the buoy data by station id"""

    req = requests.get(
        'http://www.ndbc.noaa.gov/station_page.php?station={}'
        .format(station_id)
    )

    if req.status_code != 200:
        return

    soup = BeautifulSoup(req.text, 'lxml')
    return BuoyData(
        station_id,
        parse_table_data(soup, r'Swell Height', True),
        parse_table_data(soup, r'Swell Period', True),
        parse_table_data(soup, r'Swell Direction', False)
    )


def parse_table_data(soup, label_pattern, is_num):
    """Parse data from the site"""

    pattern = re.compile(label_pattern)
    element = soup.find(text=pattern)

    if element is None:
        return None

    next_element = element.next

    if next_element is None:
        return None

    element_data = str(re.sub(r'<(/)?td>', '', str(next_element))).strip()

    if is_num:
        return re.findall(r'\d+\.\d+', element_data)[0]
    else:
        return element_data
