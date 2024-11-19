
def selection_sort(arr):
    n=len(arr)
    print(n)

    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if(arr[j] < arr[min_index]):
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr
        

arr=[8,25,33,21,50,9,5,4,8,28]
result=selection_sort(arr)
print(result)


# ----------------------------------practice
# def selection_sort(arr):
#     n=len(arr)

#     for i in range(n):
#         min_index=i

#         for j in range(i+1,n):
#             if(arr[j] < arr[min_index]):
#                 min_index=j

#         arr[i],arr[min_index]=arr[min_index],arr[i]

#     return arr


# arr=[8,4,6,2,36,76,34,3,1,9]
# result=selection_sort(arr)
# print(result)
