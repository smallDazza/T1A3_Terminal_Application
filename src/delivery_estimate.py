
from costpackage import send_code
from timepackage import del_time


def del_estimate():
    postcode_send = int(input("Please enter the postcode sending the package from: "))
    senders_list = send_code(postcode_send)

    postcode_rece = int(input("Please enter the receivers postcode: "))
    receivers_list = send_code(postcode_rece)
    
    postcode_from = senders_list[0]
    postzone_from = senders_list[1]
    postcode_to = receivers_list[0]
    postzone_to = receivers_list[1]

    delivery_time = del_time(postzone_from, postzone_to)
    for x in range(20):
            if x % 2 == 0:
                print("📦", end =" ")
            else:
                print("🚚", end =" ")
    print ("\n")
    print (f"The estimated number of days delivery time for a package between"+ 
           f"{postcode_from} and {postcode_to} is: {delivery_time} Days.\n")
    print ("Thankyou. To get a delivery cost quotation, please select number 1 from the Main Menu.")
    return

        

