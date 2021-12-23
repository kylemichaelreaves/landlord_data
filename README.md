# FindYourLandlord Data Cleaning

## Parsing and cleaning publicly available North Jersey property data
This repo is the data side of my FindYourLandlord project. I am building the UI in React with TypeScript.
As a whole, the project aims[^1] to

* Visualize property ownership in North Jersey
* Easily identify landlords owning the most property

Toward that end, **this repo** is my amateurish attempt to go from unclean data from the [Monmouth County Tax Assessor](https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11) to a Postgres database.
I went about this in the following way:

1. Clean property data
2. Geolocate the cleaned address with geopy
3. Reconcile two different kinds of property in a single table or dataframe for each city:
   - private property
   - public housing
4. Export the city's dataframe to .csv
5. Convert .csv to .geojson. Each of the features within the geojson object is a point on the map.
6. Create a Postgres database of tables from each of the cities exported dataframes

### Database / Table Schema

I caused unnecessary problems for myself by being inconsistent with casing and column names. I wrote functions to switch between cases. Those functions are in helpers.py.

- Are the psql columns and types are identical to the dataframe columns and datatypes?

```sql
CREATE TABLE jersey_city_private_property (
    id serial primary key,
    street_address text,
    owner_name text,
    owner_mailing_address text,
    city_state_zip text,
    property_full_address text,
    number_properties_owned int,
    units int,
    g_code text,
    latitude numeric(8, 6),
    longitude numeric(8, 6)
    list_properties_owned text[],
);
```

street_address
owner_name
owners_mailing_address
city_state_zip
owners_mailing_address
property_full_address
units
list_properties_owned
number_properties_owned
g_code
latitude
longitude


### Get the path of the csv we're importing to our postgres table.

`JerseyCity/JerseyCity_PublicHousing.csv`

### Import the .csv using COPY

```sql
COPY jersey_city_private_propety
FROM '/Users/kylereaves/src/landlord_data/JerseyCity/jersey_city_private_property.csv'
DELIMITER ','
CSV HEADER;
```

```sql
psql -c "\copy jersey_city_private_property FROM '/Users/kylereaves/src/landlord_data/JerseyCity/jersey_city_private_property.csv' delimiter ',' csv"
```

[^1]:
    I am not a data-scientist, and it shows. I went about this through trial and error, which is highly inefficient.
    A robust data-scientific approach would: request the data from the county tax assessor, then crawl over it.
    This would, in theory–assuming the data includes lat and long coordinates—eliminate the need to geocode the addresses
