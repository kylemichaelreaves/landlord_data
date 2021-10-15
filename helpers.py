import string, re
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="myGeolocator", timeout=2)

# all dfs must conform to this order and casing
column_order = [ 'propertyLocation',
                 'ownersName',
                 'ownersMailingAddress',
                 'cityStateZip',
                 'propertyFullAddress',
                 'units',
                 'associatedPropertyList',
                 'numberPropertiesOwned',
                 'gCode',
                 'latitude',
                 'longitude' ]

#empty df to satisfy linter
df = pd.DataFrame(columns=column_order)


def camel_to_snake(camel_string):
    return ''.join(re.sub('([A-Z]+)', r'_\1', camel_string).lower())

def snake_to_camel(snake_string):
   return re.sub('_([a-zA-Z0-9])', lambda m: m.group(1).upper(), snake_string)

# number of times owner appears in second column
def get_number_properties_owned(owner=str):
    return len(df[df.ownersName == owner])
# list of associated properties
def get_associated_properties_list(owner=str):
    return df[df.ownersName == owner]['propertyLocation'].unique().tolist()

# number of times property appears in first column
def get_units(address=str):
    return len(df[df.propertyLocation == address])

# columns and the functions that returned them
column_functions = {'ownersMailingFullAddress': df.ownersMailingAddress + ', ' + df.cityStateZip,
                    'propertyFullAddress': df.propertyLocation + '''whatever town your searching''',
                    'units': get_units(),
                    'associatedPropertyList': get_associated_properties_list(),
                    'numberOfPropertiesOwned': get_number_properties_owned(),
                    'latitude': [g.latitude for g in df.gCode],
                    'longitude': [g.longitude for g in df.gCode]
                    }