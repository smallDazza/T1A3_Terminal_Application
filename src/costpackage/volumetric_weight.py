
# Cubic Weight Function:
# Aust Post calculates cubic weight for freight = dimensions in metres multiplied by 250kg:
# The user parameters entered = cms. So converted to metres.
# The cubic weight will be rounded up to next whole kg number using
# math.ceil function from the python math module imported.

import math


def cubic_weight(length, width, height):

    length = length / 100
    width = width / 100
    height = height / 100                  # convert cms to mtrs from parameters
    cubic_weight = length * width * height
    if cubic_weight > 0.25:
        # -1 means the cubic weight is to large.
        return -1
    else:
        weight = cubic_weight * 250           # calculate cubic weight

    return math.ceil(weight)
