# Outlet-Rental
This repository lets you calculate the price of an outlet based on the rental data of near by locations.

> # How to use it ?
> - Download the three files, main.py, distanceFile and outlet_rental.csv
> - save all three files in one folder
> - run main.py

# Understanding Main.py

### file structure variables set

We'll need latitude and longitude of places from the csv file, since this file contains many other colmuns
we set the column numbers in this part of the code.

> #### Excel file structure
![Excel file](https://github.com/wilfredarin/Outlet-Rental/blob/main/file_strucutre_excel.png?raw=true)

> #### Code file structure
![Code file structure](https://github.com/wilfredarin/Outlet-Rental/blob/main/file_strucutre_code.png?raw=true)

#### Set the search area bounds
> - We'll read each latitude and longitude data line by line from our excell file and check if it falls within a box of fixed area or not.
> - If lat and lon are within the fixed area we'll calculate it's distance from our outlet else discard it.

![search_area_bounds](https://github.com/wilfredarin/Outlet-Rental/blob/main/search_area_bounds.png?raw=true)
> **search_area_box_len** contains the length of the bounding square box in metres.  
> **meter_to_coordinate** is assigned to 0.0000090909
> > 110 km is the distance between two latitudes (or distance between two longitudes) at equator  
> > i.e 1,10,000 meters = 1 degree (of latitude and longitude)  
> > 1 meter = 1/(1,10,000) degree 

> **lon_delta** is the change on either sides our outlet's longitude that we'll do, to create our search area box
> **outlet_coordinates takes in user input in the format lat, longitude (google map format : lat comma space lon)  
> > then outlet_coordinates are split lat and lon values are stored  
![outlet_coordinates_code](https://github.com/wilfredarin/Outlet-Rental/blob/main/outlet_coordinates_code.png?raw=true)  
![bounds](https://github.com/wilfredarin/Outlet-Rental/blob/main/bounds.png?raw=true)  

#### each row of csv file is read
> - lat and lon of each row is extracted and changed to float data type
> - Boundary condition is checked to ensure lat and lon falls within square bound area
> - Distance is calculated by calling **findDistance() function** and stored in **cur_distance**
> - Check if **cur_distacne** is lesser than **min_distance** then min_distacne is updated, price and complex_name is updated and **data_insuf_flag** is set to **False**
> - finaly if data_insuf_flag is True "Data insufficient" is printed else other details are printed. 


### Distancefile
#### findDistance() 
This function is used to caluclate distacne between two coordinates, to read more [follow this link](https://www.geeksforgeeks.org/program-distance-two-points-earth/)











