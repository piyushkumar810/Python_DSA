# ------------------merge sort in python

def merge(arr,left_half,right_half):
    i=j=k=0

    while i<len(left_half) and j<len(right_half):
        if(left_half[i]<right_half[j]):
            arr[k]=left_half[i]
            i+=1
        
        else:
            arr[k]=right_half[j]
            j+=1

        k+=1

    
    while(i<len(left_half)):
        arr[k]=left_half[i]
        i+=1
        k+=1

    while(j<len(right_half)):
        arr[k]=right_half[j]
        j+=1
        k+=1


def merge_sort(arr):
    n=len(arr)

    if(n>1):
        mid=n//2
        left_half=arr[ :mid]
        right_half=arr[mid: ]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr,left_half,right_half)

arr=[38,23,65,24,1,76,2,0]
print("given array is", arr)

merge_sort(arr)
print("sorted array is", arr)
