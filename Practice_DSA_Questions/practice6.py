# --------------------------- selection sort
def sel_sor(arr):
    n=len(arr)

    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
        
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

arr=[2,10,12,4,3,15]
result=sel_sor(arr)
print(result)