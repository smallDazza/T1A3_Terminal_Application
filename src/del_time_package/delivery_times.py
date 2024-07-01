# post zone charges list is globally defined
# this way ,if in the future if a module is added for 'changing delivery times' = it can be accessed.
# Delivery times based on Aust Parcel Post Delivery Estimator 2023.pdf
# To be able to match the postal_zones.py file a number of areas have been combined from above estimator pdf:
# Canberra == N2
# Far North QLD remote == Q4
# Tas Remote == T1
# Alice Springs + NT Other == NT1
# Column N1,N2,V1,V2,Q1,Q2,Q3,Q4,S1,S2,NT1,W1,W2,W3,T1


post_del_times = [
    ['2', '3-4', '2-3', '3-5', '2-3', '2-4', '3-5', '5-7', '2-4', '2-5', '4-7(Darwin)6-13(Other Areas)', '4-5', '5-8', '7-10', '3-5'],              #N1          
    ['3-4', '3-5', '3-6', ' 4-7', '4-6', '2-5', '4-7', '7-9', '3-5', '3-6', '5-9(Darwin)5-15(Other Areas)', '5-8', '5-9', '8-11', '4-7'],           #N2
    ['2-3', '4-5', '2-3', '3-4', '2-5', '3-6', '4-7', '6-8', '2-3', '3-5', '4-6(Darwin)4-14(Other Areas)', '4-5', '5-8', '8-10', '2-4'],            #V1
    ['3-4', '5-7', '2-3', '3-4', '2-5', '3-6', '5-8', '7-9', '4-6',	'3-5',	'4-8(Darwin)4-15(Other Areas)',	'5-8', '7-10', '8-11', '3-5'],          #V2
    ['2-4', '3-6', '2-5', '2-6', '2-3', '2-3', '3-7', ' 4-6', '4-7', '3-6',	'4-8(Darwin)7-14(Other Areas)',	'5-8', '7-9', '8-11', '4-6'],           #Q1
    ['2-4', '3-6', '3-5', '3-7', '2-3', '3-4', '3-5', ' 5-7', '4-6', '4-6',	'5-8(Darwin)7-16(Other Areas)',	'6-9', '7-10', '9-11', '5-7'],          #Q2
    ['3-5', '4-7', '4-7', '4-8', '3-5', '3-5', '2-5', ' 3-7', '4-8', '5-8',	'5-9(Darwin)7-16(Other Areas)',	'7-10', '7-11', '9-13',	'6-9'],         #Q3
    ['5-7', '7-9', '6-8', '7-9', '4-6', '4-6', '3-6', ' 2-5', '5-9', '6-10', '6-10(Darwin)8-18(Other Areas)', '7-10', '8-12', '9-13', '6-10'],      #Q4
    ['2-4', '4-8', '2-4', '2-6', '2-5', '3-6', '4-8', ' 5-9', '2-3', '1-3',	'3-6(Darwin)2-13(Other Areas)',	'4-5', '5-9', '8-11', '4-6'],           #S1
    ['3-5', '4-8', '2-4', '2-5', '3-6', '4-8', '5-9', ' 6-10', '2-3', '2-3', '4-6(Darwin)3-14(Other Areas)', '5-8', '6-10',	'8-10', '4-6'],         #S2
    ['4-7', '5-9', '3-6', '3-7', '4-7', '4-7', '5-10', ' 6-10',	'2-5', '4-7', '1-2(Darwin)3-10(Other Areas)', '6-9', '6-10', '8-11', '7-9'],        #NT1
    ['3-5', '4-8', '3-5', '3-8', '3-6', '4-8', '5-9', ' 7-10', '3-4', '3-6', '5-9(Darwin)4-16(Other Areas)', '2', '2-5', '4-6',	'6-8'],             #W1
    ['4-5', '4-8', '4-6', '4-7', '4-7', '5-8', '6-9', ' 8-12', '3-5', '3-6', '7-10(Darwin)6-19(Other Areas)', '2-5', '3-5',	'4-6', '8-10'],         #W2
    ['6-10', '5-11', '8-11', '7-12', '6-11', '7-12', '8-13', '9-13', '5-11', '4-8',	'7-10(Darwin)6-19(Other Areas)', '4-7',	'4-7', '2-3', '10-12'], #W3
    ['3-5', '4-7', '2-4', '3-5',' 4-6', '5-7', '6-9', '6-10', '4-6', '4-6',	'7-9(Darwin)5-15(Other Areas)',	'6-8', '8-10', '10-12',	'2-3']          #T1    
]

# This function will return the string of 'Estimated Delivery time in number of days', by the zones returned from the post_zone function (postal_zones.py file).

def del_time(zone_from, zone_to):
    return post_del_times[zone_from][zone_to]



