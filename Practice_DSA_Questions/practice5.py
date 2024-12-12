def zero(arr):
    # n=len(arr)
    non_zero=[]
    zeros=[]

    for i in arr:
        if(i != 0):
            non_zero.append(i)
        else:
            zeros.append(i)

    n=len(non_zero)
    print(non_zero)
    print(n)

    for i in range(n-1):
        for j in range(n-i-1):
            if(non_zero[j]>non_zero[j+1]):
                non_zero[j],non_zero[j+1]=non_zero[j+1],non_zero[j]
        
    return non_zero + zeros


arr=[5,2,0,0,4,3,0,1,0,0,0]
result=zero(arr)
print(result)