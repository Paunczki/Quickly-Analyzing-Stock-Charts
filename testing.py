from PIL import Image
from ArrayFromPic import ArrayFromPic as afp
from quickSort import quickSort as qs
from mergeSort import mergeSort as ms
import numpy as np
import time

def solve(input_file, output_file):
    # Load Image
    print("---Loading Image 01---", "\n")
    im = Image.open(input_file)
    array_from_pic = afp(im)
    #print(array_from_pic.mapped_array, "\n")

    # create a new 1-D array to store the different index numbers which represent for number 1. 1-D array is converting from the 2-D array's columns
    # coding by Jiaqi Fang
    columns = list(zip(*array_from_pic.mapped_array))

    # create an empty list to store the index
    arr1 = []

    oneD_array = np.empty([1,1])
    for i in range(len(array_from_pic.mapped_array)):
        oneD_array = np.array(columns[i])
        #print(oneD_array)
        for a in range(len(oneD_array)):
            if oneD_array[a] == 1:
                #print(a)
                arr1.append(a)
    print("Unsorted 1-D array: ")
    print(arr1, "\n")

    # -----------------multipule testing sorting algorithms--------------------

    # By using the recording runtime for algorithms to figure out which one is better

    # sort the data into desired order by using quickSort
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