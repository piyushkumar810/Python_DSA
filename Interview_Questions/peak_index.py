# ------------------------------by linear search

# def peak_element(arr):
#     n=len(arr)

#     if(arr[0]>arr[1]):
#         return 0
    
#     if(arr[n-1]>arr[n-2]):
#         return n-1
    
#     # if there is only one value in the list
#     if(n==1):
#         return 0
    
#     for i in range(1, n-1):
#         if(arr[i] > arr[i+1]) & (arr[i] > arr[i-1]):
#             return i


# arr=[1,3,3,4,5,4,3,3,1]
# mountain_index=peak_element(arr)
# # the mountain index will print the highest element of the index
# print(mountain_index)



# --------------------------using binary search
def peak_element(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid is the peak element
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
            return mid
        
        # If the left neighbor is greater, move to the left side
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            high = mid - 1
        
        # Otherwise, move to the right side
        else:
            low = mid + 1

    return -1  # This should never happen if input guarantees a peak element.

arr = [3, 5, 3, 2, 0]
mountain_index = peak_element(arr)
print(mountain_index)  # This will print the index of the peak element (in this case, 1)
