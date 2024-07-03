# Feature 3
import emoji
from colorama import Fore, Style
from costpackage import send_code, rece_code
from timepackage import del_time


def del_estimate():
    senders_list = send_code()

    receivers_list = rece_code()
    
    postcode_from = senders_list[0]
    zone_from = senders_list[1]
    postcode_to = receivers_list[0]
    zone_to = receivers_list[1]

    delivery_time = del_time(zone_from, zone_to)
    for x in range(20):
            if x % 2 == 0:
                print(emoji.emojize(":package:"), end =" ")
            else:
                print(emoji.emojize(":delivery_truck:"), end =" ")
    print ("\n")
    print (f"{Fore.WHITE}The estimated number of days delivery time for a package between"+ 
           f" {postcode_from} and {postcode_to} is: {Style.BRIGHT}{Fore.YELLOW}{delivery_time} Days.{Fore.RESET}\n")
    print (f"{Fore.WHITE}Thankyou. To get a delivery cost quotation, please select number 1 from the Main Menu.{Fore.RESET}\n")

    return

        

