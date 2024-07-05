
# This send-code function sneds the inputed postcode to the post_zone function (which returns a numeric zone code)
# If the code returned == -1 , the postcodes is not valid, so asks to input a new postcode.
# Keeps looping until a valid postcode returns and breaks.
from colorama import Fore, Style
from costpackage import post_zone


def send_code():
    while True:
        try:
            postcode = int(
                input(f"{Fore.CYAN}Please enter the postcode sending the package from: "))
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
                input(f"{Fore.CYAN}Please enter the receivers postcode: "))
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
