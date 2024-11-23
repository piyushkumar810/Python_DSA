# --------------------------------------bubble sort

def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

arr=[3,5,1,2,4]
result=bubble_sort(arr)
print(result)

# ---------------------------------------- selection sort

def selection_sort(arr):
    n1=len(arr1)

    for i in range(n1):
        first_element=arr[i]

        for j in range(i+1,n1):
            if(arr[j]<arr[j+1]):
                smallest_element=j




arr1=[8,25,33,21,50,9,5,37,8,28]
result1=selection_sort(arr1)
print(result1)