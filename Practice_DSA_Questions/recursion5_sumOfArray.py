# -----------------------------sum of array using recursion

def sum_of_array(arr,n):
    if(n==0):
        return 0
    else:
        return sum_of_array(arr,n-1) + arr[n-1] 
    
arr=[1,4,6,3,7,9,0]
n=len(arr)
result=sum_of_array(arr,n)
print(result)