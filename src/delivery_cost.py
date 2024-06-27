
from packages import post_zone, cubic_weight, freight_rate, zone_charge
import random
import json

def package_cost():
    delivery_job = {}
    sender_name = input("Please enter the senders name: ")
    delivery_job ["Senders Name"] = sender_name
    sender_contact = input("Please enter the senders contact number: ")
    delivery_job ["Senders Contact"] = sender_contact
    while True:
        sender_postcode = int(input("Please enter the postcode sending the package from: "))
        postcode_one = post_zone(sender_postcode)
        if postcode_one == -1:
            print("That postcode does not exist or cannot be delivered. Please try again.")
        else:
            break
    
    delivery_job ["Sender Postcode"] = sender_postcode
    receiver_name = input("Please enter the receivers name: ")
    delivery_job ["Receiver Name"] = receiver_name
    receiver_address = input("Please enter the receivers street address:  ")
    delivery_job ["Receiver Address"] = receiver_address
    while True:
        receiver_postcode = int(input("Please enter the receivers postcode: "))
        postcode_two = post_zone(receiver_postcode)
        if postcode_two == -1:
            print("That postcode does not exist or cannot be delivered. Please try again.")
        else:
            break
    
    delivery_job ["Receiver Postcode"] = receiver_postcode

    length = int(input("Please enter the package length. Length in centimetres is: "))
    width = int(input("Please enter the package width. Width in centimetres is: "))
    height = int(input("Please enter the package height. Height in centimetres is: "))

    cub_weight = cubic_weight(length, width, height)

    act_weight = int(input("Please enter the actual weight of the package. Weight in kilograms is: "))

    if length > 105 or width >105 or height > 105:
        print("Apologies but a dimension was larger than 105cm. This is to large for Aust Post to accept over the counter. Please contact for delivery options.")
        return
    elif cub_weight == -1:
        print("Apologies the cubic weight is larger than 0.25 cubic metres. This is to large for Aust Post to accept over the counter. Please contact for delivery options.")
        return
    elif act_weight > 22:
        print("Apologies but the weight is greater than 22kg. This is to large for Aust Post to accept over the counter. Please contact for delivery options.")
        return
    
    if cub_weight > act_weight:
        package_weight = cub_weight
    else:
        package_weight = act_weight
    
    freight_value = freight_rate(package_weight)

    if package_weight > 5:
        charge = zone_charge(postcode_one, postcode_two)
        delivery_cost = freight_value + (charge*(package_weight - 5))
    else:
        delivery_cost = freight_value
    
    delivery_job ["Delivery Cost"] = delivery_cost

    message = f""" 
    Here are your package delivery details based on your entries:\n
    \tSenders Name: {sender_name}\n
    \tSenders Contact Number: {sender_contact}\n
    \tSenders Postcode: {sender_postcode}\n
    \tReceivers Name: {receiver_name}\n
    \tReceivers Address: {receiver_address}\n
    \tReceivers Postcode: {receiver_postcode}\n
    \tPackage Delivery Cost: {delivery_cost}\n """
    print(message)

    while True:
        booking = input("Would you like to proceed and book this package delivery ? (Y for yes or N for no): ").upper()
        if booking == "Y":
            job_number = random.randint(10000,19999)
            delivery_job ["Delivery Ticket Number"] = job_number
            with open(f"{job_number}.json", "w") as file:
                json.dump(delivery_job, file, indent=4)
            print(f"Your delivery has been booked. Your ticket number is: {job_number}. Please record this ticket number.")
            break
        elif booking == "N":
            return
        else:
            print("Invalid option. Please select Y for Yes OR N for No")

    return








    





    



    

    
    







