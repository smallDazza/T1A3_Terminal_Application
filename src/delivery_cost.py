# Feature One will calculate the delivery cost of a package based on Australian postcodes entered.

import random
import json
import os
import math
import datetime
from colorama import Fore, Style
from costpackage import cubic_weight, freight_rate, zone_charge, send_code, rece_code


def package_cost():
    delivery_job = {}
    sender_name = input(f"{Style.BRIGHT}{Fore.CYAN}Please enter the senders name: ")
    delivery_job ["Senders Name"] = sender_name
    sender_contact = input("Please enter the senders contact number: ")
    delivery_job ["Senders Contact"] = sender_contact

    senders_list = send_code()
    delivery_job ["Sender Postcode"] = senders_list[0]

    receiver_name = input(f"{Fore.CYAN}Please enter the receivers name: ")
    delivery_job ["Receiver Name"] = receiver_name
    receiver_address = input("Please enter the receivers street address:  ")
    delivery_job ["Receiver Address"] = receiver_address

    receivers_list = rece_code()
    delivery_job ["Receiver Postcode"] = receivers_list[0]

    while True:
        try:
            print(f"{Fore.CYAN}Measurements of your package.")
            length = float(input("Please enter the package Length in centimetres: "))
            width = float(input("Please enter the package Width in centimetres: "))
            height = float(input("Please enter the package Height in centimetres: "))
        except ValueError:
            print(f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be used for measurements."+
                  f"Please start all your measurements again.{Fore.RESET}")
            continue
        while True:
            try:
                act_weight = float(input(f"{Fore.CYAN}Please enter the actual weight of the package."+
                           "Weight in kilograms is: "))
            except ValueError:
                print(f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be used for weight in kilograms.{Fore.RESET}")
                continue
            break
        break

    cub_weight = cubic_weight(length, width, height)

    if length >105 or width >105 or height >105:
        print(f"{Style.BRIGHT}{Fore.RED}Apologies but a dimension was larger than 105cm."+
              "This is to large for Australia Post to accept over the counter."+ 
              "Please contact for delivery options.")
        return
    elif cub_weight == -1:
        print(f"{Style.BRIGHT}{Fore.RED}Apologies the cubic weight is larger than 0.25 cubic metres."+
              "This is to large for Australia Post to accept over the counter."+ 
              "Please contact for delivery options.")
        return
    elif act_weight > 22:
        print(f"{Style.BRIGHT}{Fore.RED}Apologies but the weight is greater than 22kg." + 
              "This is to large for Australia Post to accept over the counter." +
              f"Please contact for delivery options.{Fore.RESET}")
        return
    
    if cub_weight > act_weight:
        package_weight = math.ceil(cub_weight)
    else:
        package_weight = math.ceil(act_weight)
    
    freight_value = freight_rate(package_weight)
    delivery_job ["Package Calculated Weight"] = package_weight

    if package_weight > 5:
        charge = zone_charge(senders_list[1], receivers_list[1])
        delivery_cost = freight_value + (charge 
                                         * (package_weight-5))
        delivery_cost = f"${delivery_cost:.2f}"
    else:
        delivery_cost = f"${freight_value}"
    
    delivery_job ["Delivery Cost"] = delivery_cost

    message = f"""{Style.BRIGHT}{Fore.CYAN}Here are your package delivery details based on your entries:\n
    \t{Fore.CYAN}Senders Name: {Fore.YELLOW}{sender_name}\n
    \t{Fore.CYAN}Senders Contact Number: {Fore.YELLOW}{sender_contact}\n
    \t{Fore.CYAN}Senders Postcode: {Fore.YELLOW}{senders_list[0]}\n
    \t{Fore.CYAN}Receivers Name: {Fore.YELLOW}{receiver_name}\n
    \t{Fore.CYAN}Receivers Address: {Fore.YELLOW}{receiver_address}\n
    \t{Fore.CYAN}Receivers Postcode: {Fore.YELLOW}{receivers_list[0]}\n
    \t{Fore.CYAN}Package Calculated Weight: {Fore.YELLOW}{package_weight}\n
    \t{Fore.CYAN}Package Delivery Cost: {Fore.YELLOW}{delivery_cost}{Fore.RESET}\n
    """
    print(message)

    # Feature 2 - If user wants to book the delivery job == writes all the delivery jod details from the delivery_job
    # dictionary to a json file.

    while True:
        booking = input(f"{Fore.CYAN}Would you like to proceed and book this package delivery ?"+ 
                        "(Y for yes or N for no): ").upper()
        if booking == "Y":
            job_number = random.randint(10000,99999)
            date_booked = datetime.date.today()
            delivery_job ["Date Booked"] = date_booked.strftime("%d-%m-%Y")
            delivery_job ["Delivery Ticket Number"] = job_number
            job_location = "delivery_jobs"
            job_path = os.path.join(job_location, f"{job_number}.json") 
            with open(job_path, "w") as file:
                json.dump(delivery_job, file, indent=4)
            print(f"Your delivery has been booked. Your ticket number is: {Fore.YELLOW}{job_number}.{Fore.RESET}"+ 
                  f"{Fore.CYAN}Please record this ticket number for future reference.\n")
            break
        elif booking == "N":
            return
        else:
            print(f"{Style.BRIGHT}{Fore.RED}Invalid option. Please enter Y for Yes OR N for No.{Fore.RESET}")

    return








    





    



    

    
    







