
# Delivery times based on Aust Parcel Post Delivery Estimator 2023.pdf
# To be able to match the postal_zones.py file a number of areas have been combined from above estimator:
# Canberra == N2
# Far North QLD remote == Q4
# Tas Remote == T1
# Alice Springs + NT Other == NT1


post_del_times = [
    [2, 3-4, 2-3, 3-5, 2-3, 2-4, 3-5, 5-7, 2-4, 2-5, 4-5, 5-8, 7-10, 3-5, 4-7]
]

str_list = [str(num) if isinstance(num, int) else f"'{num}'" for num in post_del_times]
print(str_list)

[3-4, 3-5, 3-6, 4-7, 4-6, 2-5, 4-7, 7-9, 3-5, 3-6, 5-8, 5-9, 8-11, 4-7, 5-9],