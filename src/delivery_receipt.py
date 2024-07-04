# Feature 4 - this will find the user entered ticket number and display the details of booked job.
# If user inputs Y = will write the details from json file to a text file.

import json
import os
from colorama import Fore, Style


def del_receipt():
    while True:
        try:
            ticket_num = input(f"{Style.BRIGHT}{Fore.BLUE}Please enter your delivery ticket number: ")

            ticket_path = f"delivery_jobs/{ticket_num}.json"

            with open(ticket_path, 'r') as file:
                ticket = json.load(file)
        except FileNotFoundError:                                # Error if cannot find ticket number, display message below.
            while True:
                print(f"{Fore.RED}FileNotFoundError. This ticket number {ticket_num} cannot be found.")         
                choice = input(f"Have you lost or forgotten your ticket number ? (Select Y for Yes, to return to Main Menu"+
                           f" or N for No, to re-enter a valid ticket number.): ").upper()
                if choice == "Y":
                    return
                elif choice == "N":
                     break
                else:
                    print(f"Invalid option. Select Y or N.{Fore.RESET}")
            continue
        break
# gets all these key values from the json file and saves into variables             
    senders_name = ticket["Senders Name"]
    senders_contact = ticket["Senders Contact"]
    senders_postcode = ticket["Sender Postcode"]
    receivers_name = ticket["Receiver Name"]
    receivers_address = ticket["Receiver Address"]
    receivers_postcode = ticket["Receiver Postcode"]
    package_weight = ticket["Package Calculated Weight"]
    delivery_cost = ticket["Delivery Cost"]
    date_booked = ticket["Date Booked"]
    ticket_number = ticket["Delivery Ticket Number"]

    f"{Fore.BLUE}"          
    message = f"""Here is ticket number {ticket_number}. Delivery details:\n
    \tSenders Name: {senders_name}\n
    \tSenders Contact Number: {senders_contact}\n
    \tSenders Postcode: {senders_postcode}\n
    \tReceivers Name: {receivers_name}\n
    \tReceivers Address: {receivers_address}\n
    \tReceivers Postcode: {receivers_postcode}\n
    \tPackage Calculated Weight: {package_weight}\n
    \tPackage Delivery Cost: {delivery_cost}\n
    \tDate Booked: {date_booked}\n
    """ 
    print(message)          # display all the details above from variables.

    while True:
        choice = input(f"{Fore.BLUE}Would you like to proceed and save a delivery receipt ?"+ 
                       "(Y for yes or N for no): ").upper()
        if choice == "Y":
            job_location = "delivery_receipts"
            os.makedirs(job_location, exist_ok=True)
            job_path = os.path.join(job_location, f"{ticket_number}.txt") 
            with open(job_path, "w") as txt_file:
                txt_file.write(message)                     # writes the message variable to a txt file.
            print(f"Your delivery receipt {ticket_number}.txt has been saved.\n")
            break
        elif choice == "N":
            return
        else:
            print(f"{Fore.RED}Invalid option. Please enter Y for Yes OR N for No.{Fore.RESET}")

    return


    