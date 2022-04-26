# this is pillow to install use
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

import os
from os import listdir
from os.path import isfile, join

from PIL import Image
from ArrayFromPic import ArrayFromPic
from quickSort import quickSort as qs
from mergeSort import mergeSort as ms
from algos import *
import numpy as np
import time


def test_algos(input_file, output_file):

    with open(os.path.dirname(os.path.realpath(__file__)) + '/label.txt') as file:
        labels = [line.rstrip() for line in file]

    # Get list of all names of pics in file './graphs'
    graphs_dir = os.path.dirname(os.path.realpath(__file__)) + '/graphs/'
    files = [f for f in listdir(graphs_dir) if isfile(join(graphs_dir, f))]
    graphs = []
    for f in files:
        img = Image.open(graphs_dir + f)
        afp = ArrayFromPic(img)
        graphs.append(afp)

    # Run tests for quick sort
    start_time1 = time.time()
    oneD = [twoD_to_oneD(g.mapped_array) for g in graphs]
    # print(oneD[0])
    # for g in oneD:
    #     print(len(g))
    for graph in oneD:
        qs(graph, 0, len(graph) - 1)
    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f'Quick sort took {elapsed_time1:.5f} seconds to run on {len(files)} files')

    # Run Tests for merge sort
    start_time2 = time.time()
    oneD = [twoD_to_oneD(g.mapped_array) for g in graphs]
    for graph in oneD:
        ms(graph)
    end_time2 = time.time()
    elapsed_time2 = end_time2 - start_time2
    print(f'Merge sort took {elapsed_time2:.5f} seconds to run on {len(files)} files')
    if elapsed_time1 < elapsed_time2:
        print(f'Quick sort was faster than merge sort by {elapsed_time2 - elapsed_time1:.7f} seconds\n')
    elif elapsed_time2 < elapsed_time1:
        print(f'Merge sort was faster than quick sort by {elapsed_time1 - elapsed_time2:.7f} seconds\n')
    else:
        # not likely
        print('Quick sort and merge sort took the same amount of time!\n')

    # Run tests for com_columns()
    start_time3 = time.time()
    oneD = [twoD_to_oneD(g.mapped_array) for g in graphs]
    comp_columns_result = []
    for graph in oneD:
        comp_columns_result.append(comp_columns(graph, size=len(graph) - 1))
    end_time3 = time.time()
    elapsed_time3 = end_time3 - start_time3
    results = []
    correct = 0
    for i in range(len(labels)):
        if labels[i] == comp_columns_result[i]:
            results.append(' ')
            correct += 1
        else:
            results.append('X')
    print(f'comp_columns() took {elapsed_time3:.5f} seconds to run on {len(files)} files')
    print(labels, '<-- labels')
    print(results, '<-- results')
    print(comp_columns_result, '<-- classified as')
    print(f'comp_coulmns() classified {correct}/{len(labels)} correctly\n')

    # Run tests for area()
    start_time4 = time.time()
    area_result = []
    for graph in graphs:
        area_result.append(area(graph.mapped_array))
    end_time4 = time.time()
    elapsed_time4 = end_time4 - start_time4
    results = []
    correct = 0
    for i in range(len(labels)):
        if labels[i] == area_result[i]:
            results.append(' ')
            correct += 1
        else:
            results.append('X')
    print(f'area() took {elapsed_time4:.5f} seconds to run on {len(files)} files')
    print(labels, '<-- labels')
    print(results, '<-- results')
    print(area_result, '<-- classified as')
    print(f'area() classified {correct}/{len(labels)} correctly\n')

    # Run tests for column_distance()
    start_time5 = time.time()
    column_distance_result = []
    for graph in graphs:
        column_distance_result.append(column_distance(graph.mapped_array))
    end_time5 = time.time()
    elapsed_time5 = end_time5 - start_time5
    results = []
    correct = 0
    for i in range(len(labels)):
        if labels[i] == column_distance_result[i]:
            results.append(' ')
            correct += 1
        else:
            results.append('X')
    print(f'column_distance() took {elapsed_time5:.5f} seconds to run on {len(files)} files')
    print(labels, '<-- labels')
    print(results, '<-- results')
    print(column_distance_result, '<-- classified as')
    print(f'column_distance() classified {correct}/{len(labels)} correctly\n')

    # Run tests for minima_maxima()
    start_time6 = time.time()
    minima_maxima_result = []
    for graph in graphs:
        minima_maxima_result.append(minima_maxima(graph.mapped_array))
    end_time6 = time.time()
    elapsed_time6 = end_time6 - start_time6
    results = []
    correct = 0
    for i in range(len(labels)):
        if labels[i] == minima_maxima_result[i]:
            results.append(' ')
            correct += 1
        else:
            results.append('X')
    print(f'minima_maxima() took {elapsed_time6:.5f} seconds to run on {len(files)} files')
    print(labels, '<-- labels')
    print(results, '<-- results')
    print(minima_maxima_result, '<-- classified as')
    print(f'minima_maxima() classified {correct}/{len(labels)} correctly\n')

    # Run tests for matching()
    start_time7 = time.time()
    matching_result = []
    for graph in graphs[3:]:
        matching_result.append(matching(graph.mapped_array))
    end_time7 = time.time()
    elapsed_time7 = end_time7 - start_time7
    results = []
    correct = 0
    for i in range(len(labels) - 3):
        if labels[i+3] == matching_result[i]:
            results.append(' ')
            correct += 1
        else:
            results.append('X')
    print(f'matching() took {elapsed_time7:.5f} seconds to run on {len(files) - 3} files')
    print(labels[3:], '<-- labels')
    print(results, '<-- results')
    print(matching_result, '<-- classified as')
    print(f'matching() classified {correct}/{len(labels) - 3} correctly\n')


def main():
    test_algos('graphs/Graph01.jpg', 'output01.jpg')


if __name__ == '__main__':
    main()
