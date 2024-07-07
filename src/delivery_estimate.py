# Feature 3 - provide an estimated delivery time in number of days.
import emoji
from colorama import Fore, Style
from costpackage import send_code, rece_code
from timepackage import del_time, km_distance


def del_estimate():
    # calling the same 2 functions again to return the postcodes & zones in two lists.
    # used these functions again to meet the DRY principles.
    senders_list = send_code()

    receivers_list = rece_code()

    postcode_from = senders_list[0]
    zone_from = senders_list[1]
    postcode_to = receivers_list[0]
    zone_to = receivers_list[1]
# calls the del_time function = using the 2 zone numbers to index on the
# nested list to return the delivery time.
    delivery_time = del_time(zone_from, zone_to)
    del_distance = km_distance(str(postcode_from), str(postcode_to))
    for x in range(20):
        if x % 2 == 0:
            print(emoji.emojize(":package:"), end=" ")
        else:
            print(emoji.emojize(":delivery_truck:"), end=" ")
    print("\n")
    print(
        f"{Fore.WHITE}The estimated number of days delivery time for a package between" +
        f" {postcode_from} and {postcode_to} is: {Style.BRIGHT}{Fore.YELLOW}{delivery_time} Days.{Fore.RESET}\n")
    if del_distance == -1:
        print("Sorry our data could not work out the traveling distance at this time.\n")
    else:
        print(f"{Fore.WHITE}The estimated traveling distance between these two postcodes is {Style.BRIGHT}{Fore.YELLOW}{del_distance:.2f} kms.\n")
    print(f"{Fore.WHITE}Thankyou. To get a delivery cost quotation, please select number 1 from the Main Menu.{Fore.RESET}\n")

    return
