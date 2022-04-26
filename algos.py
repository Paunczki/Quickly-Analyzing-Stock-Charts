import math

import numpy as np
from PIL import Image

from ArrayFromPic import ArrayFromPic


def twoD_to_oneD(graph):
    columns = list(zip(*graph))
    oneD_array = np.zeros(len(columns))
    mark = len(columns[0])

    for i in range(len(columns)):
        for j in range(len(columns[i])):
            if columns[i][j] == 1:
                oneD_array[i] = mark
                mark = len(columns[0])
                break
            else:
                mark -= 1
    return oneD_array


def comp_columns(graph, size=28):
    # print(size)
    column_one = graph[0]
    column_last = graph[size - 1]
    if column_one == column_last:
        return "n"
    elif column_one > column_last:
        return "-"
    elif column_last > column_one:
        return "+"


def area(graph):
    size = len(graph[0])
    l = len(graph)
    one_d = twoD_to_oneD(graph)
    above = 0
    for i in one_d:
        above += size - i
    # -1 to reduce where white box is
    tot_area = l * (size-1)
    if above > tot_area/2:
        return "+"
    elif above < tot_area/2:
        return "-"
    else:
        return "n"

def column_distance(graph):
    distance = 0
    one_d = twoD_to_oneD(graph)
    start = one_d[0]
    for i in one_d:
        distance += start - i
    if distance > 0:
        return "+"
    elif distance < 0:
        return "-"
    else:
        return "n"


def minima_maxima(graph):
    one_d = twoD_to_oneD(graph)
    prev = "n"
    prev_new = "n"
    change_array = []
    change_array.append(one_d[0])
    switch_array = []
    for i in range(len(one_d)):
        if i == 0:
            continue
        change = one_d[i] - one_d[i-1]
        if change > 0:
            prev_new = "+"
        elif change < 0:
            prev_new = "-"
        else:
            prev_new = "n"

        if prev != prev_new:
            change_array.append(one_d[i])
            if len(switch_array) == 0:
                switch_array.append(prev)
            switch_array.append(prev_new)
        prev = prev_new
    change_array.append(one_d[len(one_d)-1])
    switch_array.append(prev)

    # now contains only where shift occured
    # we can later add the change numbers as a different indicator
    pos_count = 0
    neg_count = 0
    neu_count = 0
    for i in switch_array:
        if i == "+":
            pos_count +=1
        elif i == "-":
            neg_count += 1
        else:
            neu_count += 1

    if pos_count > neg_count and pos_count > neu_count:
        return "+"
    elif neg_count > pos_count and neg_count > neu_count:
        return "-"
    else:
        return "n"


# graphs: array of graphs to be compared to
# target: target graph being compared to graphs
def matching(graph):
    ref_graphs = {'+': twoD_to_oneD(ArrayFromPic(Image.open('graphs/Graph01.jpg')).mapped_array),
                  '-': twoD_to_oneD(ArrayFromPic(Image.open('graphs/Graph02.jpg')).mapped_array),
                  'n': twoD_to_oneD(ArrayFromPic(Image.open('graphs/Graph03.jpg')).mapped_array)}
    scores = {'+': 0, '-': 0, 'n': 0}
    oneD_graph = twoD_to_oneD(graph)
    for ref in ref_graphs.keys():
        for i in range(len(ref_graphs[ref])):
            scores[ref] += abs(ref_graphs[ref][i] - oneD_graph[i])

    minimum = math.inf
    match_result = ''
    for score in scores.keys():
        if scores[score] < minimum:
            minimum = scores[score]
            match_result = score

    return match_result







