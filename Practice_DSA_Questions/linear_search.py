def linear_search(arr,target_value):
    n=len(arr)

    for i in range(n):
        if(arr[i]==target_value):
            return i
        
    return f"your target element is not in the list"


arr=[1,3,5,7,9,11,13,15,17,19]
result=linear_search(arr,11)
print(f"your target element is found at index {result}")