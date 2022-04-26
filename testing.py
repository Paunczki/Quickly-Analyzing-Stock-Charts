# this is pillow to install use
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

import os
from os import listdir
from os.path import isfile, join

from PIL import Image
from ArrayFromPic import ArrayFromPic as afp
from quickSort import quickSort as qs
from mergeSort import mergeSort as ms
from algos import *
import numpy as np
import time


def test_algos(input_file, output_file):
    # Load Image
    # print("---Loading Image 01---", "\n")
    # im = Image.open(input_file)
    # array_from_pic = afp(im)
    # for f in array_from_pic.mapped_array:
    #     print(f)


    # Get list of all names of pics in file './graphs'
    graphs_dir = os.path.dirname(os.path.realpath(__file__)) + '/graphs/'
    files = [f for f in listdir(graphs_dir) if isfile(join(graphs_dir, f))]
    graphs = []
    for f in files:
        img = Image.open(graphs_dir + f)
        graphs.append(afp(img))

    # Run tests for quick sort
    start_time = time.time()
    oneD = [twoD_to_oneD(g.mapped_array) for g in graphs]
    # print(oneD[0])
    # for g in oneD:
    #     print(len(g))
    for graph in oneD:
        qs(graph, 0, len(graph) - 1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Quick sort took {elapsed_time} seconds to run on {len(files)} files')

    # Run Tests for merge sort
    start_time = time.time()
    oneD = [twoD_to_oneD(g.mapped_array) for g in graphs]
    for graph in oneD:
        ms(graph)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Merge sort took {elapsed_time} seconds to run on {len(files)} files', '\n')

    # Run tests for com_columns()
    start_time = time.time()
    oneD = [twoD_to_oneD(g.mapped_array) for g in graphs]
    comp_columns_result = []
    for graph in oneD:
        comp_columns_result.append(comp_columns(graph, size=len(graph) - 1))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'comp_columns() took {elapsed_time} seconds to run on {len(files)} files')
    print(comp_columns_result, '\n')

    # Run tests for area()
    start_time = time.time()
    area_result = []
    for graph in graphs:
        area_result.append(area(graph.mapped_array))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'area() took {elapsed_time} seconds to run on {len(graphs)} files')
    print(area_result, '\n')

    # Run tests for column_distance()
    start_time = time.time()
    column_distance_result = []
    for graph in graphs:
        column_distance_result.append(column_distance(graph.mapped_array))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'column_distance() took {elapsed_time} seconds to run on {len(graphs)} files')
    print(column_distance_result, '\n')

    start_time = time.time()
    minima_maxima_result = []
    for graph in graphs:
        minima_maxima_result.append(minima_maxima(graph.mapped_array))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'minima_maxima() took {elapsed_time} seconds to run on {len(graphs)} files')
    print(minima_maxima_result, '\n')






    # -----------------multipule testing sorting algorithms--------------------

    # By using the recording runtime for algorithms to figure out which one is better

    # sort the data into desired order by using quickSort
    # arr1 = twoD_to_oneD(array_from_pic)

    # b = len(arr1)
    #
    # # set the starting time for quickSort
    # start_time = time.time()
    #
    # # call the quickSort
    # qs(arr1, 0, b - 1)

    # print the sorted array by using mergesort
    # print("Array sorted by quickSort is:")
    # for i in range(b):
    #     print(arr1, sep=" ")
    #     break
    #
    # # print the runtime of quickSort
    # print("The runtime of quickSort is: ")
    # stop_time = time.time()
    # runtime_qs = start_time - stop_time
    # print(f"--- {runtime_qs} seconds ---", "\n")
    #
    # # set the starting time for mergeSort
    # start_time = time.time()
    #
    # # sort the data into desired order by using mergesort
    # # call the mergeSort
    # ms(arr1)
    #
    # # print the sorted array by using mergesort
    # print("Array sorted by mergeSort is:")
    # for i in range(b):
    #     print(arr1, sep=" ")
    #     break

    # # print the runtime of mergeSort
    # print("The runtime of mergeSort is: ")
    # stop_time = time.time()
    # runtime_ms = start_time - stop_time
    # print(f"--- {runtime_ms} seconds ---")
    #
    # # comparing the runtime to determine which algorithm is faster
    # # the runtime may different each time when u run the code
    # if runtime_qs > runtime_ms:
    #     print("quickSort is slower than mergeSort in this project.", "\n")
    # elif runtime_qs < runtime_ms:
    #     print("quickSort is faster than mergeSort in this project.", "\n")
    # else:
    #     print("They have same runtime.", "\n")


def main():
    test_algos('graphs/Graph01.jpg', 'output01.jpg')


if __name__ == '__main__':
    main()
