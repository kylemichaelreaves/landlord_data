# FindYourLandlord Data Cleaning

### Parsing and cleaning publicly available North Jersey property data


#### This project aims to  
* Visualize property ownership in North Jersey
* Easily identify landlords owning the most property

#### Strategy
* Geocode the address in order to be visualized later in MapBoxGL

** I am not a data-scientist, and it shows. 
** I went about this through trial and error, which is highly inefficient.
** A robust, datas-scientific approach would be to request the data from the county tax assessor, and then put it in a database by crawling over it. 
** This would, in theory, assuming the data includes lat and long coordinates, eliminate the need to geocode the addresses. 
 
#### Table Schema and Casing
** I ran into casing and spacing issues when I wanted to transition to a larger set of features. 
** propertyLocation,ownersName,ownersMailingAddress,cityStateZip,units,propertiesOwned,numberPropertiesOwned,propertyFullAddress,gCode,Lat,Long

The data was gathered from publicly available records on the Monmouth County Tax Assesssor's website: 
https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11


This repo is the data side of my FindYourLandlord project. I am building the UI in React with TypeScript.
As a whole, the project aims[^1] to

- Visualize property ownership in North Jersey
- Easily identify landlords owning the most property

Toward that end, **this repo** is my amateurish attempt to go from unclean data from the [Monmouth County Tax Assessor](https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11) to a Postgres database.
I went about this in the following way:

0. Clean property data
1. Geolocate the cleaned address with geopy
2. Reconcile two different kinds of property in a single table or dataframe for each city:
   - private property
   - public housing
3. Export the city's dataframe to .csv
4. Convert .csv to .geojson. Each of the features within the geojson object is a point on the map.
5. Create a Postgres database of tables from each of the cities exported dataframes

## Database / Table Schema

I caused unnecessary problems for myself by being inconsistent with casing and column names. I wrote functions to switch between cases. Those functions are in helpers.py.

```sql
CREATE TABLE jersey_city_private_property (
    id serial,
    street_address text,
    owners_name text,
    owners_mailing_address text,
    city_state_zip text,
    property_full_address text,
    number_properties_owned int,
    units int,
    list_properties_owned text[],
    g_code text,
    latitude numeric(8, 6),
    longitude numeric(8, 6),
    primary key (id)
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


[^1]:
    I am not a data-scientist, and it shows. I went about this through trial and error, which is highly inefficient.
    A robust data-scientific approach would: request the data from the county tax assessor, then crawl over it.
    This would, in theory–assuming the data includes lat and long coordinates—eliminate the need to geocode the addresses
```
```sql
psql -c "\copy jersey_city_private_property FROM '/Users/kylereaves/src/landlord_data/JerseyCity/jersey_city_private_property.csv' delimiter ',' csv"
```
