# Python program for implementation of Quicksort Sort coding by Jiaqi Fang

def partition(arr, low, high):
    # index of smaller element
    i = (low-1)
    # the pivot
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The following function is the main function that implements QuickSort
# arr[] is the array needs to be sorted,
# low si the starting index,
# high is the ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr1
    if low < high:

        # pivot is partitioning index, arr[pivot] is now at right place
        pivot = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)