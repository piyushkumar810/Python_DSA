# Q) sort the string in decreasing order of the value associated after removal of value x.

def sort_the_string(str,x):

    # create the list
    my_list=str.split()

    n=len(my_list)
    print(n)
    print(my_list)
    print("\n")

    # removing the pair whose value is less than the given number
    for i in range(n-1,0,-2):
        print(my_list[i])
        if int(my_list[i])<x:
            del(my_list[i-1:i+1])
    
    print("\n")
    n=len(my_list)
    print(n)
    print(my_list)
    
    # sort the given list of elements
    for i in range(1,n,2):
        for j in range(1,n-i,2):
            if my_list[j] < my_list[j+2] or (my_list[j-1] < my_list[j+1] and my_list[j] == my_list[j+2]):
                my_list[j],my_list[j+2]=my_list[j+2],my_list[j]
                my_list[j-1],my_list[j+1]=my_list[j+1],my_list[j-1]

    return " ".join(my_list)


str="akash 43 vishal 78 mohan 96 rohit 78 shivam 49"
result=sort_the_string(str,50)
print(result)
print(type(result))