# -------------------------------binary search

# when given array is already sorted

def binary_search(arr,searching_element):
    n=len(arr)
    # print(n)

    low = 0
    high = (n-1)

    while(low <= high):

        mid=((low+high)//2)

        if(arr[mid]==searching_element):
            return mid
        
        elif(arr[mid]<searching_element):
            low=mid+1
        else:
            high=mid-1

    return -1  # target element not found


arr=[1,3,5,7,9,11,13,15,17,19]
result=binary_search(arr,13)
print(f"your element is found at index {result}")
