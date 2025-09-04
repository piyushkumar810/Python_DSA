# [3,5,7,9,1] print the number in opposit order number using recursion
def print_the_no(num_list, i):
    if(i>=len(num_list)):
        return
    else:
        print_the_no(num_list, i+1)
        print(num_list[i])

print_the_no([3,5,7,9,1], 0)