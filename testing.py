# this is pillow to install use
    # python3 -m pip install --upgrade pip
    # python3 -m pip install --upgrade Pillow 
from PIL import Image
from ArrayFromPic import ArrayFromPic as afp
from quickSort import quickSort as qs
from mergeSort import mergeSort as ms
from algos import *
import numpy as np
import time

def solve(input_file, output_file):
    # Load Image
    print("---Loading Image 01---", "\n")
    im = Image.open(input_file)
    array_from_pic = afp(im)
    
    # -----------------multipule testing sorting algorithms--------------------

    # By using the recording runtime for algorithms to figure out which one is better

    # sort the data into desired order by using quickSort
    arr1 = twoD_to_oneD(array_from_pic)

    b = len(arr1)

    # set the starting time for quickSort
    start_time_qs = time.time()

    # call the quickSort
    qs(arr1, 0, b-1)

    # print the sorted array by using mergesort
    print("Array sorted by quickSort is:")
    for i in range(b):
        print(arr1, sep = " ")
        break

    # print the runtime of quickSort
    print("The runtime of quickSort is: ")
    runtime_qs = time.time() - start_time_qs
    print("--- %s seconds ---" % runtime_qs, "\n")

    # set the starting time for mergeSort
    start_time_ms = time.time()

    # sort the data into desired order by using mergesort
    # call the mergeSort
    ms(arr1)

    # print the sorted array by using mergesort
    print("Array sorted by mergeSort is:")
    for i in range(b):
        print(arr1, sep = " ")
        break

    # print the runtime of mergeSort
    print("The runtime of mergeSort is: ")
    runtime_ms = time.time() - start_time_ms
    print("--- %s seconds ---" % runtime_ms, "\n")

    # comparing the runtime to determine which algorithm is faster
    # the runtime may different each time when u run the code
    if runtime_qs > runtime_ms:
        print("quickSort is slower than mergeSort in this project.", "\n")
    elif runtime_qs < runtime_ms:
        print("quickSort is faster than mergeSort in this project.", "\n")
    else:
        print("They have same runtime.", "\n")
    
def main():
    solve('graphs/Graph01.jpg', 'output01.jpg')

if __name__ == '__main__':
    main()