
# This freight rate function will return the package freight rate depending on its weight.


def freight_rate(package_weight): 
   if package_weight < 0.5:
      freight_value = 10.60
      return freight_value
   elif 0.5 <= package_weight <= 1:
      freight_value = 14.50
      return freight_value
   elif 1 <= package_weight <= 3:
      freight_value = 18.25
      return freight_value
   else:
      freight_value = 21.95
      return freight_value
   
# when returned to main = need to format using f"{value:.2f}" for 2 decimal places ??
