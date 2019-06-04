# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    x = 0  # i
    y = 0  # j
    z = 0  # k

    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr[z] = arrA[x]
            x = x + 1
        else:
            merged_arr[z] = arrB[y]
            y = y + 1
            z = z + 1

    while x < len(arrA):
        merged_arr[z] = arrA[x]
        x = x + 1
        z = z + 1

    while y < len(arrB):
        merged_arr[z] = arrB[y]
        y = y + 1
        z = z + 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
