# Q) push zeros too the end while maintaining the relative order of the element

def remove_zeros(my_list):
    non_zero=[]
    zeros=[]
    for i in my_list:
        if(i!=0):
            non_zero.append(i)
        else:
            zeros.append(i)
    return non_zero + zeros


my_list=[1,2,0,4,3,0,0,5,0] 
print(remove_zeros(my_list))
print("\n")

# -------------------------------------------------or

def push_zero_back(my_list1):
    for i in my_list1:
        if(i==0):
            my_list1.remove(i)
            my_list1.append(i)
    return my_list1

my_list1=[1,2,0,4,3,0,0,5,0]
result=push_zero_back(my_list1)
print(result)