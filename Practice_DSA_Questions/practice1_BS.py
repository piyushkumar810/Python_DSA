def search(nums,target):
    size_of_array=len(nums)

    low=0
    high=(size_of_array-1)

    while(low<=high):
        mid=((low+high)//2)

        if(nums[mid]==target):
            return mid

        elif(nums[mid]<target):
            low=mid+1
        else:
            high=mid-1

    return -1

nums=[-1,0,3,5,9,12]
target=int(input("enter the target element : "))
result=search(nums,target)
print(f"{target } exists in nums and its index is {result} ")