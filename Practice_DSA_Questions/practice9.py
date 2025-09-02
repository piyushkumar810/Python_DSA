# --------- QUESTION 1 --------- 
# [3,5,7,9,1] print all number using recursion
def print_no_recursively(num_list, i):
    if(i>=len(num_list)):
        return
    else:
        print(num_list[i])
    print_no_recursively(num_list, i+1)

print_no_recursively([3,5,7,9,1], 0)


#--------- QUESTION 2 ---------
# Write a Python program to calculate the sum of a list of numbers using recursion. 

def sum_of_list(num_list, i):
    if(i>=len(num_list)):
        return 0
    else:
        return num_list[i] + sum_of_list(num_list, i+1)
         
         
sum_of_list([2,3,5,7,9], 0)