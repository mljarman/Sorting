# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # to keep track of index location as elements from
    # arrA, arrB get copied into merged_arr.
    counter_A = 0
    counter_B = 0
    # If arrA runs out, add elements from arrB, if arrB runs out, add elements from arrA:
    for i in range(elements):
        if counter_A >= len(arrA):
            merged_arr[i] = arrB[counter_B]
            counter_B += 1
        elif counter_B >= len(arrB):
            merged_arr[i] = arrA[counter_A]
            counter_A += 1
        # if element in arrA is smaller, add it to merged and move to next index:
        elif arrA[counter_A] < arrB[counter_B]:
            merged_arr[i] = arrA[counter_A]
            counter_A += 1
        else:
            # if element in arrB is smaller, add it to merged_arr at that index
            # location and move to next index.
            merged_arr[i] = arrB[counter_B]
            counter_B += 1
    return merged_arr

# # TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # base case:
    # if array is empty or len 1, return
    if len(arr) <= 1:
        return arr
    else:
        # split array into half
        arr1 = arr[len(arr)//2:]
        arr2 = arr[:len(arr)//2]
        # sort each half:
        sort1 = merge_sort(arr1)
        sort2 = merge_sort(arr2)
        # use merge helper function to merge back together:
        return merge(sort1, sort2)

#
# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO
#
#     return arr
#
# def merge_sort_in_place(arr, l, r):
#     # TO-DO
#
#     return arr
#
#
# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):
#
#     return arr
