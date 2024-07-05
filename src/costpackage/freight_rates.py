
# This freight rate function will return the package freight rate
# depending on its weight.


def freight_rate(package_weight):
    if package_weight < 0.5:
        freight_value = 10.95
        return freight_value
    elif 0.5 <= package_weight <= 1:
        freight_value = 14.95
        return freight_value
    elif 1 <= package_weight <= 3:
        freight_value = 18.95
        return freight_value
    else:
        freight_value = 22.85
        return freight_value
