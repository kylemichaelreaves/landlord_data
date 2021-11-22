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