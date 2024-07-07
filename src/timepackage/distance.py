import math
import csv
import os


def km_distance(postcode1, postcode2):

    def find_csv(postcode):
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'australian_postcodes.csv')
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip headers
            for row in reader:
                if row[0] == postcode:
                    return float(row[1]), float(row[2])
        return None

    def haversine_distance(lat1, lon1, lat2, lon2):
        # distance between latitudes and longitudes
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0
 
        # convert to radians
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0
 
        # apply haversine formula
        a = (pow(math.sin(dLat / 2), 2) +
            pow(math.sin(dLon / 2), 2) *
                math.cos(lat1) * math.cos(lat2))
        c = 2 * math.asin(math.sqrt(a))
        harv_distance = 6371 * c                # 6371 = Radius of Earth in kilometers
        
        return harv_distance

# any issues with cannot find a longitude or latitude, returns -1.
    location1 = find_csv(postcode1)
    if location1 == None:
        return -1
    elif location1:
        Lat_precise1, Long_precise2 = location1      
    else:
        return -1

    location2 = find_csv(postcode2)
    if location2 == None:
        return -1
    elif location2:
        Lat_precise3, Long_precise4 = location2
        
    else:
        return -1

    distance = haversine_distance(Lat_precise1, Long_precise2, Lat_precise3, Long_precise4)
    return distance
