# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # to keep track of index location, count times element from
    # arrA, arrB replaces a 0 in merged_arr.
    counter_A = 0
    counter_B = 0
    counter_M = 0
    # while there are less elements from arrA and arrB in merged_arr
    # than elements in arrA and arrB:
    while counter_A < len(arrA) and counter_B < len(arrB):
        # if element in arrA is smaller, add it to merged and increase
        # count.
        if arrA[counter_A] < arrB[counter_B]:
            merged_arr[counter_M] = arrA[counter_A]
            counter_A += 1
            counter_M += 1
        else:
            # if element in arrB is smaller, add it to merged_arr at that index
            # location and increase count to go to next index.
            merged_arr[counter_M] = arrB[counter_B]
            counter_B += 1
            counter_M += 1
    if counter_B < len(arrB):
        while counter_M < len(merged_arr):
            # if there are still 0's in merged_arr and still unused elements in
            # arrB that haven't been added, replace the rest of the 0's with them.
            merged_arr[counter_M] = arrB[counter_B]
            counter_M += 1
            counter_B += 1
    if counter_A < len(arrA):
        while counter_M < len(merged_arr):
            # if there are still 0's in merged_arr and still unused elements in
            # arrA that haven't been added, replace the rest of the 0's with them.
            merged_arr[counter_M] = arrA[counter_A]
            counter_M += 1
            counter_A += 1
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
