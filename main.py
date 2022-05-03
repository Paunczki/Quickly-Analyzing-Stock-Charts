import os
from os import listdir
from os.path import isfile, join
from PIL import Image
from ArrayFromPic import ArrayFromPic
from quickSort import quickSort as qs
from mergeSort import mergeSort as ms
from algos import *
from add_algos import *
from imageConverter import *
import numpy as np
import time


def main(image_location):
    # First we need to convert the image into 2D array (this is done pixel to pixel)
    two_d_array = convertImage(image_location)
    one_d_array = [twoD_to_oneD(g.mapped_array) for g in [two_d_array]]

    # Here we will only show the pricing pattern algos as they will be more beneficial

    print("\nGraph:", image_location)
    start_time2 = time.time()
    # Needed for additional algorithms, might have errors
    zig_zagg, zz_vals, tops, bottoms = zig_zag(one_d_array)
    # print(zig_zagg, zz_vals, tops, bottoms)
    top_count, bottom_count = top_bot_straights(tops, bottoms)
    # print(top_count, bottom_count)
    count_tops, count_bottoms, top_avg, bottom_avg = find_lines(one_d_array[0])
    # print(count_tops, count_bottoms, top_avg, bottom_avg)

    results, val = head_and_shoulders(tops, bottoms, top_count, bottom_count)
    if results == True:
        print("\tHead & Shoulders = ", val)
    
    results, val = double_top(tops, bottoms, top_count, bottom_count)
    if results == True:
        print("\tDouble Top = ", val)

    results, val = double_bottom(tops, bottoms, top_count, bottom_count)
    if results == True:
        print("\tDouble Bottom = ", val)
    
    results, val = rounding_bottom(tops, bottoms)
    if results == True:
        print("\tRounding Bottom = ", val)
    
    results, val = wedge(count_tops, count_bottoms, top_avg, bottom_avg)
    if results == True:
        print("\tWedge = ", val)
    
    results, val = asc_traingle(count_tops, count_bottoms, top_avg, bottom_avg)
    if results == True:
        print("\tAscending Triangle = ", val)
    
    results, val = desc_triangle(count_tops, count_bottoms, top_avg, bottom_avg)
    if results == True:
        print("\tDescending Triangle = ", val)
    
    end_time2 = time.time()
    elapsed_time2 = end_time2 - start_time2
    print("Time taken:", elapsed_time2)
