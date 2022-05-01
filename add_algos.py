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

def find_lines(oneD_array):
    # This is a generic function to take the 1D Array and reduce it
    #   to its peaks/valleys
    # Will return the y values and x values in separate
    prev = -1
    direc = 1
    # keep track of prev and dir to know if there is a change
    # Follow 1, -1 for up, down
    tops = []
    bottoms = []
    # Have arrays for points where switch
    # Arrays should keep track of which point they were at to keep time 

    # Lets work backwards based on above requirements we set
    # this would mean that direction is actually opposite
    l = len(oneD_array) - 1
    for j in range(l):
        if j == 0:
            prev = oneD_array[l]
            continue
        if prev < oneD_array[l-j] and direc == 1:
            # top
            print("Switch up")
            tops.append(l-j)
            if len(bottoms) == 0:
                bottoms.append(l)
            prev = oneD_array[l-j]
            direc = -1
        elif prev > oneD_array[l-j] and direc == -1:
            # bottom
            print("Switch down")
            bottoms.append(l-j)
            if len(tops) == 0:
                tops.append(l)
            prev = oneD_array[l-j]
            direc = 1
        # Below are not needed because they are moving in constant direction
        '''
        elif prev > i and direc == 1:
            print("Continuing in direction")
        elif prev < i and direc == -1:
            print("Continue in direction")
        else:
            print("Same, do nothing")
        '''
    # return tops, bottoms
    start = "o"
    if tops[0] > bottoms[0]:
        start = "t"
    else:
        start = "b"
    
    zig_zag = []

    if start == "t":
        for i in range(len(tops)):
            zig_zag.append(tops[i])
            zig_zag.append(bottoms[i])
    elif start == "b":
        for i in range(len(bottoms)):
            zig_zag.append(bottoms[i])
            zig_zag.append(tops[i])
    
    zz_vals = []
    for j in zig_zag:
        zz_vals.append(oneD_array[j])

    # array is in reverse order
    if len(zig_zag) == 0:
        return False, 0
    # Need a j value for when zig-zag stops
    # Then need to evaluate if that is a growth
    top_slope = []
    bottom_slope = []
    sum_top = 0
    sum_bottom = 0

    for t in range(len(tops)):
        if t != (len(tops)-1):
            delta_y = oneD_array[tops[t]] - oneD_array[tops[t+1]]
            delta_x = tops[t] - tops[t+1]
            slope = delta_y/delta_x
            top_slope.append(slope)
            sum_top += slope

    for b in range(len(bottoms)):
        if b != (len(bottoms)-1):
            delta_y = oneD_array[bottoms[b]] - oneD_array[bottoms[b+1]]
            delta_x = bottoms[b] - bottoms[b+1]
            slope = delta_y/delta_x
            bottom_slope.append(slope)
            sum_bottom += slope
    
    top_avg = sum_top / len(tops)
    bottom_avg = sum_bottom / len(bottoms)

    count_tops = 0
    for i in tops:
        p_diff = math.abs(i-top_avg) / top_avg
        if p_diff > 0.2:
            # If difference is more than 20%, the breakthrough
            #   may have already happened, return false
            break
        count_tops += 1

    count_bottoms = 0
    for i in bottoms:
        p_diff = math.abs(i-bottom_avg) / bottom_avg
        if p_diff > 0.2:
            break
        count_bottoms += 1
    
    return count_tops, count_bottoms, top_avg, bottom_avg


def wedge(count_tops, count_bottoms, top_avg, bottom_avg):
    # For a wedge we want to  see a zig-zag in price, but within a range
    # count_tops, count_bottoms, top_avg, bottom_avg = find_lines(oneD_array)
    if count_tops < 2 or count_bottoms < 2:
        return False, 0

    # At this point, we know a wedge exists
    # Now we need to return the direction
    if top_avg > 0 and bottom_avg > 0:
        # for a wedge, w/ pos slope, breakout down, and viceversa
        return True, -1
    elif top_avg < 0 and bottom_avg < 0:
        return True, 1
    else:
        # This will be a check in case something was missed
        return False, 0

# Pennant is basically a smaller asc/desc triangle
# Commented out for now as we handle this by checking for 
#   at least 2 points that fit within scope
'''
def pennant(count_tops, count_bottoms, top_avg, bottom_avg):
    if count_tops < 2 or count_bottoms < 2:
        return False, 0

    if top_avg < 0 and bottom_avg > 0:
        return True, 1
    else:
        return False, 0
'''

# Remove Symmetrical Tringles as below is better use of the patterns


def asc_traingle(count_tops, count_bottoms, top_avg, bottom_avg):
    if count_tops < 2 or count_bottoms < 2:
        return False, 0

    # We need an additional check to see if positive trend upwards but bottom is growing faster than converges too
    # We will use 0.67 as it means that bottom is growing faster
    if (top_avg <= 0 and bottom_avg > 0) or (top_avg > 0 and bottom_avg > 0 and top_avg/bottom_avg < 0.67):
        return True, 1
    else:
        return False, 0


def desc_triangle(count_tops, count_bottoms, top_avg, bottom_avg):
    if count_tops < 2 or count_bottoms < 2:
        return False, 0

    # Reverse what was in ascending triangle
    if (top_avg < 0 and bottom_avg <= 0) or (top_avg < 0 and bottom_avg < 0 and bottom_avg/top_avg < 0.67):
        return True, -1
    else:
        return False, 0

