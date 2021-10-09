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