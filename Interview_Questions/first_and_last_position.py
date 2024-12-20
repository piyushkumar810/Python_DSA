# Q) find the first and lastt position of the sorrted array


#------------------------------------ solving with linear search

def first_and_last(arr,target):
    n=len(arr)
    first=-1
    last=-1
    
    for i in range(n):
        if(target != arr[i]):
            continue

        if(first == -1):
            first = i

        last=i

    return [first , last]


arr=[1,3,4,6,6,6,8,9]
target=int(input("enter the element for which you want the first and last index = "))
result=first_and_last(arr,target)
print(result)


# ------------------------solving with binary search (this way we will get best time complexity)

# def first_and_last(arr,target):
#     n=len(arr)
#     low=0
#     high=n-1

#     while(low<=high):
#         mid=((low+high)//2)

        

# arr=[1,3,4,6,6,6,8,9]
# target=int(input("enter the element for which you want the first and last index = "))
# result=first_and_last(arr,target)
# print(result)