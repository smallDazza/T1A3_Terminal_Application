
# This send-code function sneds the inputed postcode to the post_zone function (which returns a numeric zone code)
# If the code returned == -1 , the postcodes is not valid, so asks to input a new postcode.
# Keeps looping until a valid postcode returns and breaks.

from costpackage import post_zone


def send_code(postcode):
    while True:
        zone = post_zone(postcode)
        if zone == -1:
            print("That postcode does not exist or cannot be delivered by Australia Post."+ 
                  "Please try again.")
            new_postcode = int(input("Please enter a new postcode: "))
            postcode = new_postcode
        else:
            break
    return [postcode, zone]
        

