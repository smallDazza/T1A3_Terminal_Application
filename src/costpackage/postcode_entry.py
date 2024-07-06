
# This send_code & rece_code functions send the inputed postcode to the post_zone function (which returns a numeric zone code)
# A while loop is used so:
# If the code returned == -1 , the postcodes is not valid = asks to input a new postcode.
# if a ValueError occurs = warns users and asks again.
# Keeps looping until a valid postcode returns and breaks.
import emoji
from colorama import Fore, Style
from costpackage import post_zone


def send_code():
    while True:
        try:
            postcode = int(
                input(f"{Fore.CYAN}{emoji.emojize(':postbox:')} Please enter the postcode sending the package from: "))
        except ValueError:
            print(
                f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be entered for postcodes.{Fore.RESET}")
            continue
        zone = post_zone(postcode)
        if zone == -1:
            print(
                f"{Fore.RED}That postcode does not exist or cannot be delivered by Australia Post." +
                f"Please try again.{Fore.RESET}")

        else:
            break
    return [postcode, zone]


def rece_code():
    while True:
        try:
            postcode = int(
                input(f"{Fore.CYAN}{emoji.emojize(':postbox:')} Please enter the receivers postcode: "))
        except ValueError:
            print(
                f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be entered for postcodes.{Fore.RESET}")
            continue
        zone = post_zone(postcode)
        if zone == -1:
            print(
                f"{Fore.RED}That postcode does not exist or cannot be delivered by Australia Post." +
                f"Please try again.{Fore.RESET}")

        else:
            break
    return [postcode, zone]
