# FindYourLandlord Data Cleaning
This repo is the data side of my FindYourLandlord project.
UI in React with TypeScript. I'm implementing a Rails version and a Django version. 

## Source
For reasons unknown, Monmouth County hosts all of the property tax records for the state of New Jersey. 
The data is from the [Monmouth County Tax Assessor](https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11)

## Strategy 
1. Clean property data: use a regex to extract or split a string
2. Geolocate the cleaned address with geopy 
3. Add the geocoded address as a new column in the dataframe.
4. Export the city's dataframe to .csv
5. Convert .csv to .geojson. Each of the features within the geojson object is a point on the map.
6. Create a Postgres database of tables from each of the cities exported dataframes

### Database / Table Schema
In the interest of saving time and avoiding frustration, maintain consistent **spelling**, **casing**, and **column order**
across dataframes, models, and tables. 
If the columns appear differently in a Rails schema than they do in a .csv, Rails won't be able to seed the model.


### Get the path of the csv we're importing to our postgres table.

`JerseyCity/JerseyCity_PublicHousing.csv`

### Import the .csv using COPY in SQL

```sql
COPY jersey_city_private_propety
FROM '/Users/kylereaves/src/landlord_data/JerseyCity/jersey_city_private_property.csv'
DELIMITER ','
CSV HEADER;
```

```sql
psql -c "\copy jersey_city_private_property FROM '/Users/kylereaves/src/landlord_data/JerseyCity/jersey_city_private_property.csv' delimiter ',' csv"
```
