
# Australia Post Parcel Charges zones commented below (from the pdf). Note: Area #NF for Norfolk Island has not been used for this application.
# This function will return a numeric code from the postcode(s) entered by user.

def post_zone(postcode):
    if postcode < 800 or postcode >= 10000:
        return -1
    elif 800 <= postcode <= 999:
        return 10           #NT1              
    elif 1000 <= postcode <= 2263 or 2500 <= postcode <= 2530 or 2555 <= postcode <= 2574 or 2740 <= postcode <= 2786 or postcode == 2890:
        return 0            #N1
    elif 2264 <= postcode <= 2499 or 2531 <= postcode <= 2554 or 2575 <= postcode <= 2730 or 2787 <= postcode <= 2889 or 2891 <= postcode <= 2999:
        return 1            #N2
    elif 3000 <= postcode <= 3220 or 3335 <= postcode <= 3341 or 3425 <= postcode <= 3443 or 3750 <= postcode <= 3811 or 3910 <= postcode <= 3920 or 3926 <= postcode <= 3944 or 3972 <= postcode <= 3978 or 3980 <= postcode <= 3983 or 8000 <= postcode <= 8999:
        return 2            #V1
    elif 2731 <= postcode <= 2739 or 3221 <= postcode <= 3334 or 3342 <= postcode <= 3424 or 3444 <= postcode <= 3749 or 3812 <= postcode <= 3909 or 3921 <= postcode <= 3925 or 3945 <= postcode <= 3971 or 3984 <= postcode <= 3999 or postcode == 3979:
        return 3            #V2
    elif 4000 <= postcode <= 4225 or 4226 <= postcode <= 4299 or 4500 <= postcode <= 4549 or 9000 <= postcode <= 9299 or 9400 <= postcode <= 9596 or 9700 <= postcode <= 9799:
        return 4            #Q1
    elif 4300 <= postcode <= 4449 or 4550 <= postcode <= 4699 or 9597 <= postcode <= 9599 or 9880 <= postcode <= 9919:
        return 5            #Q2
    elif 4450 <= postcode <= 4499 or 4700 <= postcode <= 4805 or 9920 <= postcode <= 9959:
        return 6            #Q3
    elif 4806 <= postcode <= 4899:
        return 7            #Q4
    elif 5000 <= postcode <= 5199 or 5800 <= postcode <= 5999:
        return 8            #S1
    elif 5200 <= postcode <= 5749:
        return 9            #S2
    elif 6000 <= postcode <= 6214 or 6800 <= postcode <= 6999:
        return 11           #W1
    elif 6215 <= postcode <= 6699:
        return 12           #W2
    elif 6700 <= postcode <= 6797:
        return 13           #W3
    elif 7000 <= postcode <= 7999:
        return 14           #T1
    else:
        return -1
    
