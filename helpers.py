import string
import re
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="myGeolocator", timeout=2)

# all dfs must conform to this order and casing
COLUMNS = ['street_address',
           'owner_name',
           'owner_mailing_address',
           'city_state_zip',
           'owner_full_mailing_address',
           'property_full_address',
           'units_at_property',
           'g_code',
           'latitude',
           'longitude',
           'number_properties_owned',
           'list_properties_owned',]
# empty df to satisfy linter
df = pd.DataFrame(columns=COLUMNS)


def camel_to_snake(camel_string):
    return ''.join(re.sub('([A-Z]+)', r'_\1', camel_string).lower())


def snake_to_camel(snake_string):
    return re.sub('_([a-zA-Z0-9])', lambda m: m.group(1).upper(), snake_string)


# number of times owner appears in second column
def get_number_properties_owned(owner=str):
    return len(df[df.owner_name == owner])


# list of associated properties
def get_associated_properties_list(owner=str):
    return df[df.owner_name == owner]['street_address'].to_list()


# number of times property appears in first column
def get_units(address=str):
    return len(df[df.street_address == address])


# columns and the functions that returned them
column_functions = {'owner_mailing_address': df.owner_mailing_address + ', ' + df.city_state_zip,
                    'property_full_address': df.street_address + '''whatever town your searching''',
                    'units': get_units(),
                    'list_associated_properties': get_associated_properties_list(),
                    'number_properties_owned': get_number_properties_owned(),
                    'latitude': [g.latitude for g in df.g_code],
                    'longitude': [g.longitude for g in df.g_code]
                    }
