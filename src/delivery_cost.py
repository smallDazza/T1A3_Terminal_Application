# Feature One 

import random
import json
import os
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
            length = int(input("Please enter the package Length in centimetres: "))
            width = int(input("Please enter the package Width in centimetres: "))
            height = int(input("Please enter the package Height in centimetres: "))
        except ValueError:
            print(f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be used for measurements."+
                  f"Please start all your measurements again.{Fore.RESET}")
            continue
        while True:
            try:
                act_weight = int(input(f"{Fore.CYAN}Please enter the actual weight of the package."+
                           "Weight in kilograms is: "))
            except ValueError:
                print(f"{Style.BRIGHT}{Fore.RED}ValueError. Only numbers can be used for weight in kilograms.{Fore.RESET}")
                continue
            break
        break

    cub_weight = cubic_weight(length, width, height)

    if length > 105 or width >105 or height > 105:
        print(f"{Style.BRIGHT}{Fore.RED}Apologies but a dimension was larger than 105cm."+
              "This is to large for Australia Post to accept over the counter."+ 
              "Please contact for delivery options.")
        return
    elif cub_weight == -1:
        print("Apologies the cubic weight is larger than 0.25 cubic metres."+
              "This is to large for Australia Post to accept over the counter."+ 
              "Please contact for delivery options.")
        return
    elif act_weight > 22:
        print("Apologies but the weight is greater than 22kg." + 
              "This is to large for Australia Post to accept over the counter." +
              f"Please contact for delivery options.{Fore.RESET}")
        return
    
    if cub_weight > act_weight:
        package_weight = cub_weight
    else:
        package_weight = act_weight
    
    freight_value = freight_rate(package_weight)
    delivery_job ["Package Calculated Weight"] = package_weight

    if package_weight > 5:
        charge = zone_charge(senders_list[1], receivers_list[1])
        delivery_cost = freight_value + (charge 
                                         * (package_weight-5))
    else:
        delivery_cost = freight_value
    
    delivery_job ["Delivery Cost"] = delivery_cost

    f"{Style.BRIGHT}{Fore.CYAN}"
    message = f"""Here are your package delivery details based on your entries:\n
    \tSenders Name: {sender_name}\n
    \tSenders Contact Number: {sender_contact}\n
    \tSenders Postcode: {senders_list[0]}\n
    \tReceivers Name: {receiver_name}\n
    \tReceivers Address: {receiver_address}\n
    \tReceivers Postcode: {receivers_list[0]}\n
    \tPackage Calculated Weight: {package_weight}\n
    \tPackage Delivery Cost: {delivery_cost:.2f}\n
    """
    print(message)
    # Feature 2
    while True:
        booking = input("Would you like to proceed and book this package delivery ?"+ 
                        "(Y for yes or N for no): ").upper()
        if booking == "Y":
            job_number = random.randint(10000,99999)
            delivery_job ["Delivery Ticket Number"] = job_number
            job_location = "delivery_jobs"
            job_path = os.path.join(job_location, f"{job_number}.json") 
            with open(job_path, "w") as file:
                json.dump(delivery_job, file, indent=4)
            print(f"Your delivery has been booked. Your ticket number is: {Fore.YELLOW}{job_number}.{Fore.RESET}"+ 
                  f"{Fore.CYAN}Please record this ticket number for future reference.")
            break
        elif booking == "N":
            return
        else:
            print(f"{Style.BRIGHT}{Fore.RED}Invalid option. Please enter Y for Yes OR N for No.{Fore.RESET}")

    return








    





    



    

    
    







