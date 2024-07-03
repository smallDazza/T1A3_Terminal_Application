# T1A3: Terminal Application.
## Package Delivery Application.

### GitHub Repository Link: [GitHub Repository](https://github.com/smallDazza/T1A3_Terminal_Application)

## Application Scope:

This Package Delivery Application is to provide users an estimated delivery cost and delivery time for any items they are wanting to send within Australia based on their inputs of the package dimensions and weight. Should the user decide to go ahead with the quoted delivery, the application will generate a job delivery ticket number. This ticket number can also be used by the user to save a delivery receipt with all the delivery job details for future reference.

## Application Feature Outline:
### **Main Menu**: 
***Description*** - When users run the application the first area to be displayed is the Main Menu. This is where users can choose one of the features to use. There are 4 options: Package Delivery Cost Calculator, Estimate Package Delivery Times, Save a Delivery Receipt and Exit Application.

Logic - The main menu logic is located in the main.py file. This file is importing th following Python packages:
1. emoji package. 
2. colorama package.
When users enter their choice number for the feature they want to use, it will then call the corresponding function imported from the file location. Entering the following numbers will call the following functions:
 - Number 1 --> will call the 'package_cost' function, located in the 'delivery_cost.py' file.
 - Number 2 --> will call the 'del_estimate' function, located in the 'delivery_estimate.py' file.
 - Number 3 --> will call the 'del_receipt' function, located in the 'delivery_receipt.py' file.
 - Number 4 --> will exit the application.

Main Menu Image:

![Main Menu](./docs/App%20Main%20Menu.png)
____________________________________________________________

### **Feature One**
**Package Delivery Cost Calculator:**
***Description*** - The Package Delivery Cost Calculator will estimate a delivery charge based on a number of user entered data inputs. This feature has been based on the current 2024 Australia Post Parcel Charges for the standard parcel delivery service only. These can be viewed from this pdf:
[Australia Post Parcel Regular Service Charges 2024, Based on Pages 15,16 & 17 Rates](https://auspost.com.au/content/dam/auspost_corp/media/documents/post-guides/post-charges-guide-ms11.pdf)

The user inputs are:
 - Sender name & contact number.
 - Sender postcode.
 - Receiver name & address.
 - Receiver postcode.
 - Package dimensions of length, width and height. Entered in centremetres.
 - Package weight. Entered in kilograms.

From the postcodes, dimensions and weight inputs a package delivery cost will be calculated.
These will all be displayed to the user, who can choose to book the delivery job or not.

Feature One Image:

![Feature One](./docs/Feature%20One%20image.png)

***Logic*** - The 'delivery_cost.py' file is importing the following Python packages:
1. Random package.
2. Json package.
3. Os package.
4. Math package.
5. Colorama package.
6. The costpackage & importing the following functions and their uses:
 - send_code & rece_code from the postcode_entry.py file :
    - postcode_entry.py also imports post_zone from the postal_zones.py file = this uses the user postcodes entered to find & return a zone number the postcode belongs to.
    - send_code & rece_code functions handle if the postcodes entered by user are not valid. If so, asks the user to re-enter another postcode. Continues until a valid postcode entered. Then returns both valid postcode and zone number it belongs to, as a list format.
 - cubic_weight from the volumetric_weight.py file = this calculates the cubic weight of the package based on the user inputs of length, width and height. 
 - freight_rate from the freight_rates.py file = based on the package weight to use, this returns a delivery rate for 4 different levels of package weight. The rate levels are: less than 0.5kg, between 0.5kg & 1kg, between 1kg & 3kg and then above 3kg. 
 - zone_charge from the zone_surcharge.py file = should the weight to use be greater than 5kg, this file has a nested list to find the extra surcharge to be used based on the zone number returned in the post_zone function.

Based on the user dimensions inputed, a cubic weight will be calculated. The greater of the two weights (weight entered or cubic weight), will be used as the package weight for the delivery cost. Their are 4 standard package weight rates upto 5kgs.If the package weight is above 5kg, then there is a extra surcharge rate for every extra 1kg (or part thereof) based on the two postcode zones.
All the user inputs of sender name & contact, receiver name & address, postcodes, the package weight used and the delivery cost will be saved to a dictionary called delivery_job.

NOTE:
Australia Post DO NOT accept packages based on 3 values:
1. A maximum package weight of 22kg.
2. A maximum any dimension of 105cm.
3. A maximum cubic dimension of 0.25 cubic metres.
If any one of these are entered by user or calculated, a warning will display advising the user to contact Aust Post for further instructions and return them to the main menu.

### **Feature Two**
**Save Delivery Job Details As A json File**
**Description** - After the feature one displays delivery details, the user is asked if they would like to book this delivery job by a 'Y or N' response. If user chooses to book the delivery job, a delvery ticket number will be displayed for their future reference and all the details saved as a json file, named as the ticket number.

Feature two Image:

![ticket number json file](./docs/Feature%20Two%20image.png)

**Logic** - For feature two, at the top of the delivery_cost file, it is importing 3 Python packages:
1. Random module using the randint function = to generate a random number.
2. json module using the dump function = to write a json file.
3. os module using the join function = to join the json file path components.
 - If user enters a 'N' the application will return to the main menu. If 'Y' a random number will be generated, this will be assigned as the job ticket number, added to the delivery_job dictionary. Then the entire delivery_job dictionary will be written as a json file and saved as the ticket number in the delivery_jobs folder. 

### **Feature Three**
**Estimate Package Delivery Times:**
***Description*** - This feature for Estimate Package Delivery Times will ask the user to enter 2 postcode numbers, the senders postcode and the receivers postcode. Based on the 2 postcodes entered and the the postal zones they belong to, the application will display an estimated delivery time in number of days to the user. This feature has been based on the estimates from the Australia Post parcel post delivery estimator grid 2023. These can be viewed from this pdf:
[Australia Post Transit Grid Delivery Estimator 2023 - Page 2 Parcel Post](https://auspost.com.au/content/dam/auspost_corp/media/documents/domestic-parcels-delivery-estimator.pdf)

Feature Three Image:

![feature Three](./docs/Feature%20Three%20image.png)

***Logic*** - 
 - In the delivery_estimate.py file, is the del_estimate function. From both the costpackage & timepackage packages, the delivery_estimate file is importing the following functions and their uses:
 - send_code & rece_code functions from the postcode_entry.py file. This is re-used in exactly the same way a what it is in feature one.
 - del_time function from the delivery_times file. This function will return a specific delivery time in the number of days based on the postal zones the postal codes belong to.

The sender and receiver postcodes inputed from the post_zone function will return the postal zones these postcodes belong to. Then these zones will be used on the delivery_daytimes list of delivery times (for the same zones), which return the exact estimated delivery times (row, column) between the 2 postal code zones according to the AusPost Transit Grid Delivery Estimator August 2023 update pdf.

### **Feature Four**
**Save A Delivery Receipt**
***Description:*** - This feature will find a delivery ticket number entered by the user, then display the delivery job details of this ticket and ask the user if thay would like to save a receipt of this delivery job. If 'No' = then returns to the main menu. If 'Yes', it will save all of the details displayed of this delivery job to a text file to the 'delivery_receipts' folder.

Feature Four Image:

![Feature Four](./docs/Feature%20Four%20image.png)

***Logic*** - The delivery_receipt.py file will import 2 Python packages:
1. json module using the load function = to read a json file.
2. os module using the join & makedirs functions = to join the txt file path components & check the folder location exists.
The del_receipt function will ask for a ticket number, then search & find this numbered json file located in the delivery_jobs folder. The individual values of this json ticket number will be then saved into variables and displayed to the user.

The user will be asked to save a delivery receipt or not. If No = returns to main menu. If Yes = saves all the string variables to a text file located in the delivery_receipts folder.

## Package Delivery Application Design :

### Application Pseudocode:
The application psuedocode has been designed in this pdf document:

[Package Delivery Application Pseudocode pdf](./docs/T1A3%20Pseudocode.pdf)

### Application Flowchart :
The application flowchart has has been designed using drawio. Please see the below image:

![Package Delivery Application Flowchart](./docs/Package%20Delivery%20App%20Flowchart.png)

### Project Management Kanban Board :
For the design and development steps of the Package Delivery Application, I have used a kanban board from Trello:

Trello board - start project:

![Trello board start](./docs/Trello%20start.png)

Trello board - main setup and design done, start development:

![Trello board -start development](./docs/Trello%20start%20coding.png)

Trello board - testing phase:

![Trello board - testing phase](./docs/Trello%20testing%20phase.png)

Trello board - completed:


### Application Feature Ticket Tasks :
Please see images for the tasks in each feature ticket.
Feature One:

![Feature One](./docs/Feature%20one%20ticket%20tasks.png)

Feature Two:

![Feature Two](./docs/Feature%20two%20ticket%20tasks.png)

Feature Three:

![Feature Three](./docs/Feature%20Three%20ticket%20tasks.png)

Feature Four:

![Feature Four](./docs/Feature%20Four%20ticket%20tasks.png)

### Code Styling Guide :
In coding the application using the Python language and using Visual Studio Code as the IDE. The Python style guide adhered to is 'PEP 8 – Style Guide for Python Code'.
This PEP 8 style guide can be found here:

[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)








