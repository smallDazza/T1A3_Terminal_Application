
from del_cost_package import send_code
from del_time_package import del_time


def del_estimate():
    postcode_send = int(input("Please enter the Postcode sending the package from: "))
    senders_list = send_code(postcode_send)

    postcode_rece = int(input("Please enter the Receivers Postcode: "))
    receivers_list = send_code(postcode_rece)
    
    post_code_from = senders_list[0]
    post_zone_from = senders_list[1]
    post_code_to = receivers_list[0]
    post_zone_to = receivers_list[1]

    delivery_time = del_time(post_zone_from, post_zone_to)
    for x in range(20):
            if x % 2 == 0:
                print("📦", end =" ")
            else:
                print("🚚", end =" ")
    print ("\n")
    print (f"The estimated number of days delivery time for a package between {post_code_from} and {post_code_to} is: {delivery_time} Days.\n")
    print ("Thankyou. To get a delivery cost quotation, please select number 1 from the Main Menu.")
    return

        

