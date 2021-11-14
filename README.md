# FindYourLandlord Data Cleaning

### Parsing and cleaning publicly available North Jersey property data

This repo is the data side of my FindYourLandlord project. I am building the UI in React with TypeScript.
As a whole, the project aims[^1] to

- Visualize property ownership in North Jersey
- Easily identify landlords owning the most property

Toward that end, **this repo** is my amateurish attempt to go from unclean data from the [Monmouth County Tax Assessor](https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11) to a Postgres database.
I went about this in the following way:

0. Clean property data
0. Geolocate the cleaned address with geopy
0. Reconcile two different kinds of property in a single table or dataframe for each city:
    - private property
    - public housing
0. Export the city's dataframe to .csv
0. Convert .csv to .geojson. Each of the features within the geojson object is a point on the map.
0. Create a Postgres database of tables from each of the cities exported dataframes

## Database / Table Schema
I caused unnecessary problems for myself by being inconsistent with casing and column names. I wrote are text casing functions in helpers.py for changing from one to the other.

```sql
CREATE TABLE jersey_city (
    id serial,
    street_address text,
    owner_name text,
    owners_mailing_address text,
    city_state_zip text,
    property_full_address text,
    units int,
    list_properties_owned text[],
    number_properties_owned int,
    g_code text,
    latitude numeric(8, 6),
    longitude numeric(8, 6),
    primary key (id)
);
```

Get the path of the csv we're importing to our postgres table.
`JerseyCity/JerseyCity_PublicHousing.csv`


[^1]:
    I am not a data-scientist, and it shows. I went about this through trial and error, which is highly inefficient.
    A robust data-scientific approach would: request the data from the county tax assessor, then crawl over it.
    This would, in theory–assuming the data includes lat and long coordinates—eliminate the need to geocode the addresses
