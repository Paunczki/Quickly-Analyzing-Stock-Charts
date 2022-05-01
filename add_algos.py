import math
import numpy as np
from ArrayFromPic import ArrayFromPic

# for these lets send over 1D Array as input
# This makes sense as drawing on the graph depends on knowing y-vals

# Additionally, for each algo we return back boolean of 
#    if that pricing pattern was found, and the direction it should head
# To do this, we will have the following values
#       -1 --> DOWN
#        0 --> Neutral / Not Found
#        1 --> UP

# Note: It should only return true if the breakout has not begun yet
# What this means is that if pricing is already skyrocketing up,
#    it can reverse at any point and therefore is not worth investing in

# To do the above, run through the entire 1D array and have simple
#    check to see if 

def wedge(oneD_array):
    # For a wedge we want to 
    print("Wedge")
    return False, "0"


def pennant(oneD_array):
    print("Pennant")
    return False, "-1"


def sym_triangle(oneD_array):
    print("Symmetrical Triangle")
    return False, "0"


def asc_traingle(oneD_array):
    print("Ascending Triangle")
    return False, "0"


def desc_triangle(oneD_array):
    print("Descending Triangle")
    return False, "0"

