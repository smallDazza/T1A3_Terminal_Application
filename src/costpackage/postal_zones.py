
# Australia Post Parcel zones (from the Parcel Post Charges pdf). Note: Area #NF for Norfolk Island has not been used for this application.
# This function will return a numeric code of the zone each postcode falls within, entered by user.
# return -1 = a postcode entered that does not exist.


def post_zone(postcode):
    if postcode < 800 or postcode >= 10000:
        return -1
    elif 800 <= postcode <= 999:                                    #NT1
        return 10                         
    elif (1000 <= postcode <= 2263 or 2500 <= postcode <= 2530 
          or 2555 <= postcode <= 2574 or 2740 <= postcode <= 2786 
          or postcode == 2890):                                     #N1
        return 0            
    elif (2264 <= postcode <= 2499 or 2531 <= postcode <= 2554 
          or 2575 <= postcode <= 2730 or 2787 <= postcode <= 2889 
          or 2891 <= postcode <= 2999):                             #N2
        return 1            
    elif (3000 <= postcode <= 3220 or 3335 <= postcode <= 3341 
          or 3425 <= postcode <= 3443 or 3750 <= postcode <= 3811 
          or 3910 <= postcode <= 3920 or 3926 <= postcode <= 3944 
          or 3972 <= postcode <= 3978 or 3980 <= postcode <= 3983 
          or 8000 <= postcode <= 8999):                             #V1
        return 2            
    elif (2731 <= postcode <= 2739 or 3221 <= postcode <= 3334 
          or 3342 <= postcode <= 3424 or 3444 <= postcode <= 3749 
          or 3812 <= postcode <= 3909 or 3921 <= postcode <= 3925 
          or 3945 <= postcode <= 3971 or 3984 <= postcode <= 3999 
          or postcode == 3979):                                     #V2
        return 3            
    elif (4000 <= postcode <= 4225 or 4226 <= postcode <= 4299 
          or 4500 <= postcode <= 4549 or 9000 <= postcode <= 9299 
          or 9400 <= postcode <= 9596 or 9700 <= postcode <= 9799): #Q1
        return 4            
    elif (4300 <= postcode <= 4449 or 4550 <= postcode <= 4699 
          or 9597 <= postcode <= 9599 or 9880 <= postcode <= 9919): #Q2
        return 5            
    elif (4450 <= postcode <= 4499 or 4700 <= postcode <= 4805 
          or 9920 <= postcode <= 9959):                             #Q3
        return 6            
    elif 4806 <= postcode <= 4899:                                  #Q4
        return 7            
    elif 5000 <= postcode <= 5199 or 5800 <= postcode <= 5999:      #S1
        return 8            
    elif 5200 <= postcode <= 5749:                                  #S2
        return 9            
    elif 6000 <= postcode <= 6214 or 6800 <= postcode <= 6999:      #W1
        return 11           
    elif 6215 <= postcode <= 6699:                                  #W2
        return 12           
    elif 6700 <= postcode <= 6797:                                  #W3
        return 13           
    elif 7000 <= postcode <= 7999:                                  #T1
        return 14           
    else:
        return -1
    