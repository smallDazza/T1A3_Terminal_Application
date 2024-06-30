
from packages import post_zone


def delivery_time():
    zone_delivery_times = {
        0: "Next Day Delivery",
        1: "2 Day Delivery",
        2: "2-3 Day Delivery",
        3: "3-4 Day Delivery",
        4: "4-5 Day Delivery",
        5: "5-7 Day Delivery"
    }

    sender_postcode = int(input("Please enter the postcode sending the package from: ""))
    post_zone(sender_postcode)
    receiver_postcode = post_zone(receiver_postcode)
    
    del_times = post_zone_from - post_zone_to
    del_times = abs(del_times)
    for zone in zone_delivery_times:
        if zone == del_times:
            return zone_delivery_times[zone]
