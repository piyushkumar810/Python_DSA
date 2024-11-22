# given a sorted array and an integer 'x', find the lower bound of the x.


# linear search for finding lower bond

# def lower_bound(arr,x):
#     n=len(arr)
#     for i in range(n):
#         if(arr[i] >= x):
#             return i

# arr=[1,2,3,3,6,8,9]
# x=int(input("Enter the value you want the lower bound : "))
# lower_bound_index=lower_bound(arr,x)
# print(lower_bound_index)



# binary search for finding lower bond

def lower_bound_optimal(arr,x):
    n=len(arr)
    low=0
    high=(n-1)
    ans=n

    while(low <= high):
        mid=((low+high)//2)

        if(arr[mid]>=x):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

arr=[1,2,3,3,6,8,9]
x=int(input("Enter the value you want the lower bound : "))
lower_bound_index=lower_bound_optimal(arr,x)
print(lower_bound_index)
