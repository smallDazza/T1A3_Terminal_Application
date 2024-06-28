# Main Menu Function
# 

from delivery_cost import package_cost
# from delivery_time import delivery_time
# from receipt import delivery_receipt


def main_menu():
    for x in range(20):
        if x % 2 == 0:
            print("📦", end =" ")
        else:
            print("🚚", end =" ")

    print("\n")
    print("\tWelcome to the Package Delivery Application.\n")
    message = """Important To Note:\nThis application is based on delivery costs & times from Australia Post.\nApplication costings DO NOT include packaging. Items must be in their own packaging.\n
    """  
    print (message)
    while True:
        for x in range(20):
            if x % 2 == 0:
                print("📦", end =" ")
            else:
                print("🚚", end =" ")
        print("\n")
        print("Main Menu Options:\n")
        print("\t1 - 💰 Package Deivery Cost Calculator.\n")
        print("\t2 - ⏱️  Estimate Package Delivery Time.\n")
        print("\t3 - 🧾 Save a Delivery Receipt.\n")
        print("\t4 - 👋 Exit Application.\n")
        choice = int(input("Please type the number for your option selection: "))
        
        if choice == 1:
            package_cost()
            
        elif choice == 2:
            delivery_time()
            
        elif choice == 3:
            delivery_receipt()
            
        elif choice == 4:
            return
        else:
            print("This is invalid ⚠️. Please enter a number from 1 to 4.")          
    

if __name__ == "__main__":
    main_menu()

     