
from packages import post_zone

def send_code(postcode):
    
    while True:
        postcode_one = post_zone(postcode)
        if postcode_one == -1:
            print("That postcode does not exist or cannot be delivered. Please try again.")
            postcode_one = int(input("Please enter the postcode sending the package from: "))
            continue
        else:
            break    
    return postcode_one
        

def receive_code(postcode):
    while True:
        postcode_two = post_zone(postcode)
        if postcode_two == -1:
            print("That postcode does not exist or cannot be delivered. Please try again.")
            postcode_two = int(input("Please enter the receivers postcode: "))
            break
        else:
            return postcode_two

