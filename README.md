# FindYourLandlord Data Cleaning

### Parsing and cleaning publicly available North Jersey property data

The larger project aims[^1] to

- Visualize property ownership in North Jersey
- Easily identify landlords owning the most property

Toward that end, this repo specifically aims to

- Clean property data
- Geolocate the cleaned address with geopy
- Reconcile two different kinds of property in one table for each city:
- - private property
- - public housing

[^1]:
    I am not a data-scientist, and it shows. I went about this through trial and error, which is highly inefficient.
    A robust data-scientific approach would: request the data from the county tax assessor, then crawl over it.
    This would, in theory–assuming the data includes lat and long coordinates—eliminate the need to geocode the addresses

The data was gathered from publicly available records on the Monmouth County Tax Assesssor's website:
https://tax1.co.monmouth.nj.us/cgi-bin/prc6.cgi?menu=index&ms_user=monm&passwd=data&district=1301&mode=11
