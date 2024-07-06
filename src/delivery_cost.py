# Feature One will calculate the delivery cost of a package based on
# Australian postcodes entered.

import random
import json
import os
import math
import datetime
import emoji
from prettytable import PrettyTable
from colorama import Fore, Style
from costpackage import cubic_weight, freight_rate, zone_charge, send_code, rece_code


def package_cost():
    delivery_job = {}
    sender_name = input(
        f"{Style.BRIGHT}{Fore.CYAN}Please enter the {emoji.emojize(':person:')} senders name: ")
    delivery_job["Senders Name"] = sender_name
    sender_contact = input(f"{Fore.CYAN}Please enter the senders {emoji.emojize(':telephone_receiver:')} contact number: ")
    delivery_job["Senders Contact"] = sender_contact

    senders_list = send_code()
    delivery_job["Sender Postcode"] = senders_list[0]

    receiver_name = input(f"{Fore.CYAN}Please enter the {emoji.emojize(':person:')} receivers name: ")
    delivery_job["Receiver Name"] = receiver_name
    receiver_address = input(f"{Fore.CYAN}Please enter the receivers {emoji.emojize(':houses:')} street address:  ")
    delivery_job["Receiver Address"] = receiver_address

    receivers_list = rece_code()
    delivery_job["Receiver Postcode"] = receivers_list[0]

    while True:
        try:
            print(f"\n{emoji.emojize(':straight_ruler:')}{Fore.CYAN} Measurements of your package {emoji.emojize(':package:')}.")
            length = float(
                input("Please enter the package Length in centimetres: "))
            width = float(
                input("Please enter the package Width in centimetres: "))
            height = float(
                input("Please enter the package Height in centimetres: "))
        except ValueError:
            print(
                f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be used for measurements." +
                f"Please start all your measurements again.{Fore.RESET}")
            continue
        while True:
            try:
                act_weight = float(
                    input(
                        f"{Fore.CYAN}Please enter the {emoji.emojize(':balace_scale:')} actual weight of the package {emoji.emojize(':package:')} ." +
                        "Weight in kilograms is: "))
            except ValueError:
                print(
                    f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be used for weight in kilograms.{Fore.RESET}\n")
                continue
            break
        break

    cub_weight = cubic_weight(length, width, height)

    if length > 105 or width > 105 or height > 105:
        print(
            f"{Style.BRIGHT}{Fore.RED}Apologies but a dimension was larger than 105cm." +
            "This is to large for Australia Post to accept over the counter." +
            "Please contact for delivery options.\n")
        return
    elif cub_weight == -1:
        print(
            f"{Style.BRIGHT}{Fore.RED}Apologies the cubic weight is larger than 0.25 cubic metres." +
            "This is to large for Australia Post to accept over the counter." +
            "Please contact for delivery options.\n")
        return
    elif act_weight > 22:
        print(
            f"{Style.BRIGHT}{Fore.RED}Apologies but the actual weight is greater than 22kg." +
            "This is to heavy for Australia Post to accept over the counter." +
            f"Please contact for delivery options.{Fore.RESET}\n")
        return

    if cub_weight > act_weight:
        package_weight = math.ceil(cub_weight)
    else:
        package_weight = math.ceil(act_weight)

    freight_value = freight_rate(package_weight)
    delivery_job["Package Calculated Weight"] = package_weight

    if package_weight > 5:
        charge = zone_charge(senders_list[1], receivers_list[1])
        delivery_cost = freight_value + (charge
                                         * (package_weight - 5))
        delivery_cost = f"${delivery_cost:.2f}"
    else:
        delivery_cost = f"${freight_value}"

    delivery_job["Delivery Cost"] = delivery_cost

# Display all the details from variables in a nice looking table format.
    message = f"\n{Style.BRIGHT}{Fore.CYAN}{emoji.emojize(':package:')} {emoji.emojize(':deliver_truck:')} Here are your package delivery details based on your entries: {Fore.RESET}\n"
    table = PrettyTable()
    table.field_names = [
        F"{Style.BRIGHT}{Fore.CYAN}Delivery Fields {Fore.RESET}",
        f"{Fore.CYAN}Your Details {Fore.RESET}"]
    table.add_rows([[f"{Fore.CYAN}Senders Name: {Fore.RESET}",
                     f"{Fore.YELLOW}{sender_name}{Fore.RESET}"],
                    [f"{Fore.CYAN}Senders Contact Number: {Fore.RESET}",
                     f"{Fore.YELLOW}{sender_contact}{Fore.RESET}"],
                    [f"{Fore.CYAN}Senders Postcode: {Fore.RESET}",
                     f"{Fore.YELLOW}{senders_list[0]}{Fore.RESET}"],
                    [f"{Fore.CYAN}Receivers Name: {Fore.RESET}",
                     f"{Fore.YELLOW}{receiver_name}{Fore.RESET}"],
                    [f"{Fore.CYAN}Receivers Address: {Fore.RESET}",
                     f"{Fore.YELLOW}{receiver_address}{Fore.RESET}"],
                    [f"{Fore.CYAN}Receivers Postcode: {Fore.RESET}",
                     f"{Fore.YELLOW}{receivers_list[0]}{Fore.RESET}"],
                    [f"{Fore.CYAN}Package Calculated Weight: {Fore.RESET}",
                     f"{Fore.YELLOW}{package_weight}{Fore.RESET}"],
                    [f"{Fore.CYAN}Package Delivery Cost: {Fore.RESET}",
                     f"{Fore.YELLOW}{delivery_cost}{Fore.RESET}"]])
    print(message)
    print(table)

    # Feature 2 - If user wants to book the delivery job == writes all the delivery jod details from the delivery_job
    # dictionary to a json file.

    while True:
        booking = input(
            f"{Fore.CYAN}Would you like to proceed and book this package delivery ?" +
            "( Y for yes or N for no ): ").upper()
        if booking == "Y":
            job_number = random.randint(10000, 99999)
            date_booked = datetime.date.today()
            delivery_job["Date Booked"] = date_booked.strftime("%d-%m-%Y")
            delivery_job["Delivery Ticket Number"] = job_number
            job_location = "delivery_jobs"
            job_path = os.path.join(job_location, f"{job_number}.json")
            with open(job_path, "w") as file:
                json.dump(delivery_job, file, indent=4)
            print(
                f"{emoji.emojize(':package:')} {emoji.emojize(':delivery_truck:')} Your delivery has been booked. Your ticket number is: {Fore.YELLOW}{job_number}.{Fore.RESET}" +
                f"{Fore.CYAN}Please record this ticket number for future reference.\n")
            break
        elif booking == "N":
            return
        else:
            print(
                f"{Style.BRIGHT}{Fore.RED}Invalid option. Please enter Y for Yes OR N for No.{Fore.RESET}")

    return
