# Feature 4 - this will find the user entered ticket number and display the details of booked job.
# If user inputs Y = will write the details from json file to a text file.

import json
import os
from prettytable import PrettyTable
from colorama import Fore, Style


def del_receipt():
    while True:
        try:
            ticket_num = input(
                f"{Style.BRIGHT}{Fore.BLUE}Please enter your delivery ticket number: ")

            ticket_path = f"delivery_jobs/{ticket_num}.json"

            with open(ticket_path, 'r') as file:
                ticket = json.load(file)
        # Error if cannot find ticket number, display message below.
        except FileNotFoundError:
            while True:
                print(
                    f"{Fore.RED}FileNotFoundError. This ticket number {ticket_num} cannot be found.")
                choice = input(
                    f"Have you lost or forgotten your ticket number ? (Select Y for Yes, to return to Main Menu" +
                    f" or N for No, to re-enter a valid ticket number.): ").upper()
                if choice == "Y":
                    return
                elif choice == "N":
                    break
                else:
                    print(f"Invalid option. Select Y or N.{Fore.RESET}")
            continue
        break
# Gets all these key values from the json file and saves into variables
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

# This file data variable is the sting to write to the txt file.
    file_data = f"""Here is ticket number {ticket_number}. Delivery details:\n
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
# Display all the details from variables in a nice looking table format.
    heading = f"\n{Style.BRIGHT}{Fore.BLUE}Here is ticket number {ticket_number}. Delivery details:{Fore.RESET}\n"
    table = PrettyTable()
    table.field_names = [
        F"{Style.BRIGHT}{Fore.BLUE}Delivery Fields {Fore.RESET}",
        f"{Fore.CYAN}Your Details {Fore.RESET}"]
    table.add_rows([[f"{Fore.BLUE}Senders Name: {Fore.RESET}",
                     f"{Fore.YELLOW}{senders_name}{Fore.RESET}"],
                    [f"{Fore.BLUE}Senders Contact Number: {Fore.RESET}",
                     f"{Fore.YELLOW}{senders_contact}{Fore.RESET}"],
                    [f"{Fore.BLUE}Senders Postcode: {Fore.RESET}",
                     f"{Fore.YELLOW}{senders_postcode}{Fore.RESET}"],
                    [f"{Fore.BLUE}Receivers Name: {Fore.RESET}",
                     f"{Fore.YELLOW}{receivers_name}{Fore.RESET}"],
                    [f"{Fore.BLUE}Receivers Address: {Fore.RESET}",
                     f"{Fore.YELLOW}{receivers_address}{Fore.RESET}"],
                    [f"{Fore.BLUE}Receivers Postcode: {Fore.RESET}",
                     f"{Fore.YELLOW}{receivers_postcode}{Fore.RESET}"],
                    [f"{Fore.BLUE}Package Calculated Weight: {Fore.RESET}",
                     f"{Fore.YELLOW}{package_weight}{Fore.RESET}"],
                    [f"{Fore.BLUE}Package Delivery Cost: {Fore.RESET}",
                     f"{Fore.YELLOW}{delivery_cost}{Fore.RESET}"],
                    [f"{Fore.BLUE}Date Booked: {Fore.RESET}",
                     f"{Fore.YELLOW}{date_booked}{Fore.RESET}"],
                    [f"{Fore.BLUE}Delivery Ticket Number: {Fore.RESET}",
                     f"{Fore.YELLOW}{ticket_number}{Fore.RESET}"],])
    print(heading)                      
    print(table)                            

    while True:
        choice = input(
            f"{Fore.BLUE}Would you like to proceed and save a delivery receipt ?" +
            "(Y for yes or N for no): ").upper()
        if choice == "Y":
            job_location = "delivery_receipts"
            os.makedirs(job_location, exist_ok=True)
            job_path = os.path.join(job_location, f"{ticket_number}.txt")
            with open(job_path, "w") as txt_file:
                # writes the message variable to a txt file.
                txt_file.write(table)
            print(
                f"Your delivery receipt {ticket_number}.txt has been saved.\n")
            break
        elif choice == "N":
            return
        else:
            print(
                f"{Fore.RED}Invalid option. Please enter Y for Yes OR N for No.{Fore.RESET}")

    return
