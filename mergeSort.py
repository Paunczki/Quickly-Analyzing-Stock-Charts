# Python program for implementation of mergesort coding by Jiaqi Fang

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the middle point of the array
        mid = len(arr)//2

        # Dividing the array elements into 2 half, left half and right half
        left = arr[:mid]
        right = arr[mid:]

        # Sorting the left half
        mergeSort(left)

        # Sorting the right half
        mergeSort(right)

        i = a = b = 0

        # Copying data to temporary arrays both of left[] and right[]
        while i < len(left) and a < len(right):
            if left[i] < right[a]:
                arr[b] = left[i]
                i += 1
            else:
                arr[b] = right[a]
                a += 1
            b += 1

        # Checking if any element was left
        while i < len(left):
            arr[b] = left[i]
            i += 1
            b += 1

        while a < len(right):
            arr[b] = right[a]
            a += 1
            b += 1