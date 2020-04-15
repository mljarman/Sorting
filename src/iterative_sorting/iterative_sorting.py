# TO-DO: Complete the selection_sort() function below
arr = [5, 2, 1, 6, 8, 10]
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)-1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # iterate over list after initial loop:
        for x in range(cur_index, len(arr)):
            print(arr)
            # if value at index is smaller, it becomes smallest_index
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        # swap index locations with smallest element:
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr
selection_sort(arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through array:
    # first one will go through list once
    for i in range(len(arr)-1):
        # iterate over rest of list but don't
        # need last index because know those are largest elements.
        for x in range(len(arr)-i-1):
            print(arr)
        # compare each element to its neighbor:
        # if element on the left is higher, switch places:
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x +1], arr[x]

    return arr

# bubble_sort(arr)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
