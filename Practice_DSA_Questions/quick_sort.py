# ----------------------quick sort in python

# def quick_sort(arr):
#     if (len(arr)<=1):
#         return arr
#     else:
#         pivot=arr[len(arr)//2]
#         left=[x for x in arr if x<pivot]
#         right=[x for x in arr if x>pivot]
#         middle=[x for x in arr if x==pivot]

#         return quick_sort(left) + middle + quick_sort(right)
    
# arr=[10,7,8,9,1,5]
# result=quick_sort(arr)
# print("sorted array =", result)


# ----------------------------previous program took lots of space complexity so,
# more optimized way of code

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort_recursive(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort_recursive(arr,low,pi-1)
        quick_sort_recursive(arr,pi+1,high)

arr=[10,7,8,9,1,5]
quick_sort_recursive(arr,0,len(arr)-1)
print("sorted array =", arr)