# Q) sort the string in decreasing order of the value associated after removal of value x.


def sort_the_string(str,x):

    # create the list
    my_list=str.split()

    n=len(my_list)

    # removing the pair whose value is less than the given number
    for i in range(n-1,0,-2):
        print(my_list[i])




str="akash 43 vishal 78 mohan 96 rohit 78 shivam 49"
sort_the_string(str,50)