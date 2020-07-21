# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    # this is the base case which at this point the start point is greater or equal to the end point
    if end >= start:
        # we then declare a middle point
        middle = (start + end) // 2
        # if the target value is located at the middle then we return the middle
        if arr[middle] == target:
            return middle
        # if the target is smaller then the middle value then we move it to the left subarray
        elif arr[middle] > target:
            # recurse, towards base case
            return binary_search(arr, target, start, middle-1)
        # if the targer is greater or equal to the middle value then we move that value to the right subarray
        else:
            # recurse, towards base case
            return binary_search(arr, target, middle+1, end)

    else:
        return -1  # target wasn't found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here
