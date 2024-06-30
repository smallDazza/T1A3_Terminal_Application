
from del_cost_package import post_zone


def delivery_time():
    zone_delivery_times = {
        0: "2 Day Delivery",
        1: "2 Day Delivery",
        2: "2-3 Day Delivery",
        3: "3-4 Day Delivery",
        4: "4-5 Day Delivery",
        5: "5-7 Day Delivery",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "4 or more days ",
        11: "",
        12: "",
        13: "",
        14: ""


    }

def delivery_time():
    sender_postcode = int(input("Please enter the postcode sending the package from: "))
    post_zone_from = post_zone(sender_postcode)

    receiver_postcode = int(input("Please enter the Receivers Postcode: "))
    post_zone_to = post_zone(receiver_postcode)
    if post_zone_from == -1 or post_zone_to == -1:
        print("Sorry, one of the postcodes entered does not exist or cannot be delivered by Australia Post. You will be directed back to the Main Menu.")
        return
    del_times = post_zone_from - post_zone_to
    del_times = abs(del_times)
    for zone in zone_delivery_times:
        if zone == del_times:
            value = zone_delivery_times[zone]
            print (f"The estimated delivery time for this delivery is {value}")
            print ("Thankyou. To get a delivery cost quotation, please select number 1 from the Main Menu. ")
        else:
            print ("Sorry, our system cannot obtain a estimated delivery time.")
    
    return

