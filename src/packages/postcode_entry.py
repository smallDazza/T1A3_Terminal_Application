
from packages import post_zone

def send_code(postcode):
    while True:
        zone = post_zone(postcode)
        if zone == -1:
            print("That postcode does not exist or cannot be delivered by Aust Post. Please try again.")
            new_postcode = int(input("Please enter a new postcode: "))
            postcode = new_postcode
        else:
            break
    return [postcode, zone]
        

