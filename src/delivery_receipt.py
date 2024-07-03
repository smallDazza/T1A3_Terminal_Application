# Feature 4

import json
import os
from colorama import Fore, Style


def del_receipt():
    ticket_num = input(f"{Style.BRIGHT}{Fore.BLUE}Please enter your delivery ticket number: ")
    ticket_path = f"delivery_jobs/{ticket_num}.json"

    with open(ticket_path, 'r') as file:
        ticket = json.load(file)

    senders_name = ticket["Senders Name"]
    senders_contact = ticket["Senders Contact"]
    senders_postcode = ticket["Sender Postcode"]
    receivers_name = ticket["Receiver Name"]
    receivers_address = ticket["Receiver Address"]
    receivers_postcode = ticket["Receiver Postcode"]
    package_weight = ticket["Package Calculated Weight"]
    delivery_cost = ticket["Delivery Cost"]
    ticket_number = ticket["Delivery Ticket Number"]

    message = f"Here is ticket number {ticket_number}. Delivery details:\n"
    f"\tSenders Name: {senders_name}\n"
    f"\tSenders Contact Number: {senders_contact}\n"
    f"\tSenders Postcode: {senders_postcode}\n"
    f"\tReceivers Name: {receivers_name}\n"
    f"\tReceivers Address: {receivers_address}\n"
    f"\tReceivers Postcode: {receivers_postcode}\n"
    f"\tPackage Calculated Weight: {package_weight}\n"
    f"\tPackage Delivery Cost: {delivery_cost:.2f}\n" 
    print(message)

    while True:
        choice = input("Would you like to proceed and save a delivery receipt ?"+ 
                       "(Y for yes or N for no): ").upper()
        if choice == "Y":
            job_location = "delivery_receipts"
            os.makedirs(job_location, exist_ok=True)
            job_path = os.path.join(job_location, f"{ticket_number}.txt") 
            with open(job_path, "w") as txt_file:
                txt_file.write(message)
            print(f"Your delivery receipt {ticket_number}.txt has been saved.")
            break
        elif choice == "N":
            return
        else:
            print(f"{Fore.RED}Invalid option. Please enter Y for Yes OR N for No.{Fore.RESET}")

    return


    