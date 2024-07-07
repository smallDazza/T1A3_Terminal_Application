# Main Menu Function

import emoji
from colorama import Fore, Style
from delivery_cost import package_cost
from delivery_estimate import del_estimate
from delivery_receipt import del_receipt


def main_menu():
    for x in range(20):
        if x % 2 == 0:
            print(emoji.emojize(":package:"), end=" ")
        else:
            print(emoji.emojize(":delivery_truck:"), end=" ")

    print("\n")
    print(
        f"\t{Style.BRIGHT}{Fore.GREEN}Welcome to the Package Delivery Application.\n")
    message = f"""{Fore.RED}Important To Note:\n
    This application is based on standard delivery costs & times from Australia Post.\n
    Application costings DO NOT include express services or packaging.\n
    Item dimensions larger than 105cm, 0.25 cubic size or weight heavier than 22kg, cannot be accepted.\n{Fore.RESET}
    """
    print(message)
    while True:
        for x in range(20):
            if x % 2 == 0:
                print(emoji.emojize(':package:'), end=" ")
            else:
                print(emoji.emojize(':delivery_truck:'), end=" ")
        print(f"{Style.BRIGHT}{Fore.GREEN}\n")
        print("Main Menu Options:\n")
        print(
            f"\t{Fore.CYAN}1 - {emoji.emojize(':money_bag:')} Package Deivery Cost Calculator.{Fore.RESET}\n")
        print(
            f"\t{Fore.WHITE}2 - {emoji.emojize(':stopwatch:')}  Estimate Package Delivery Times & Distance.{Fore.RESET}\n")
        print(
            f"\t{Fore.BLUE}3 - {emoji.emojize(':receipt:')} Save a Delivery Receipt.{Fore.RESET}\n")
        print(
            f"\t{Fore.RED}4 - {emoji.emojize(':waving_hand:')} Exit Application.{Fore.RESET}\n")
        try:
            choice = int(
                input(f"{Fore.GREEN}Please type the number for your option selection: "))

            if choice == 1:
                package_cost()

            elif choice == 2:
                del_estimate()

            elif choice == 3:
                del_receipt()

            elif choice == 4:
                return
# This else & except = is to pick up any errors (user inputing the
# incorrect format (numbers) required) and allow program to continue.
            else:
                print(
                    f"{Fore.RED}This is invalid {emoji.emojize(':warning:')}. Please enter a number from 1 to 4.")
        except ValueError:
            print(
                f"{Fore.RED}Value Error. Only the numbers listed can be entered.{Style.RESET_ALL}")


if __name__ == "__main__":
    main_menu()
