import csv
from distanceFile import findDistance


#file strucutre
outlet_rental_file = 'outlet_rental.csv'
#columns No  in the file 
lat_col = 6
lon_col = 7
rate_col = 10
complex_col = 4

#search area box in meters
search_area_box_len = 1000
search_area_box = search_area_box_len*search_area_box_len

#110km -> 1 degree | 110*1000 m - > 1 degree | 1 m ->
meter_to_coordinate = 0.0000090909

lat_delta = meter_to_coordinate*(search_area_box_len)/2
lon_delta = meter_to_coordinate*(search_area_box_len)/2

print("************************************")
print("")
print("****Check Outlet Rental****")
print("")

outlet_coordinates = input("Enter Outlet Coordinates : ")

#eg 21.0003, 29.0004 -> split by "," coordinates ->[21.0003,29.0004]
outlet_coordinates = outlet_coordinates.split(",")
outlet_lat = float(outlet_coordinates[0])
outlet_lon = float(outlet_coordinates[1][1:])

lon_west_bound = outlet_lon -lon_delta;
lon_east_bound = outlet_lon+lon_delta;
lat_north_bound = outlet_lat+lat_delta;
lat_south_bound = outlet_lat-lat_delta;





with open(outlet_rental_file,"r") as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)
	min_distance = float('inf')
	price = 0
	complex_name = ""
	#No Rental detail in vicinity
	data_insuf_flag = True
	for row in csvreader:
		lat = float(row[lat_col])
		lon = float(row[lon_col])
		if (lat<lat_north_bound and lat>lat_south_bound):
			if lon<lon_east_bound and lon>lon_west_bound:
				cur_distance = findDistance(lat,lon,outlet_lat,outlet_lon)
				if cur_distance<min_distance:
					min_distance = cur_distance
					price = row[rate_col]
					complex_name = row[complex_col]
				data_insuf_flag = False
	if data_insuf_flag:
		print("")
		print("######################")
		print("Data is Insufficiant")
	else:
		print("##########################")
		print("")
		print("Nearest Locality is ",complex_name)
		print("Distance From outlet ",min_distance," meters")
		print("")
		print("Outlet Rental price is Rs.",price," Per square km")