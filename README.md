# FindYourLandlord Data Cleaning

### Parsing and cleaning publicly available North Jersey property data

This repo is the data side of my FindMyLandlord project. I am building the UI in React with TypeScript.
As a whole, the project aims[^1] to

- Visualize property ownership in North Jersey
- Easily identify landlords owning the most property

Toward that end, **this repo** aims to reconstruct my amateurish attempt to go from unclean data from the [Monmouth County Tax Assessor's website](https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11) to a Postgres database.
That process proceeded in the following way:

0. Clean property data
0. Geolocate the cleaned address with geopy
0. Reconcile two different kinds of property in a single table or dataframe for each city:
    - private property
    - public housing
0. Convert .csv to .geojson 
0. Export the city's dataframe to .csv
0. Create a Postgres database of tables from each of the cities exported dataframes

[^1]:
    I am not a data-scientist, and it shows. I went about this through trial and error, which is highly inefficient.
    A robust data-scientific approach would: request the data from the county tax assessor, then crawl over it.
    This would, in theory–assuming the data includes lat and long coordinates—eliminate the need to geocode the addresses

The data was gathered from publicly available records on the Monmouth County Tax Assesssor's website:
https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11
