# sort the string in decreasing order of the value associated after removal of value x.
# if marks are same the arrange the students according to the alphabitical order 

def sort_string(str,x):
    my_list=str.split()
    print(f"total students are with marks : {my_list}")

    n=len(my_list)
    print(f"length of total student {n}")

    # deleting the student how is failed in the exam
    for i in range(n-1,0,-2):
        if(int(my_list[i])<x):
            del(my_list[i-1:i+1])
    
    print(f"the remaining students are : {my_list}")
    n=len(my_list)
    print(f"new length of list = {n}")

    # remainig students should be arranged in decreasing order
    for i in range(1,n,2):   #agar range(n) tak leta tho deepak , gaurav ye sab aa jata or humko only no chaiye
        for j in range(1,n-i,2):
            if(int(my_list[j])>int(my_list[j+2])) or (int(my_list[j])==int(my_list[j+2]) and my_list[j-1]>my_list[j+1]):
                my_list[j],my_list[j+2]=my_list[j+2],my_list[j]
                my_list[j-1],my_list[j+1]=my_list[j+1],my_list[j-1]

    return " ".join(my_list)



str="anand 49 deepak 78 gaurav 95 chaman 78 ragav 46"
x=int(input("the passing number of the student so that failed student will disqualified = "))
result=sort_string(str,x)
print(result)




# --------------------------------------need to remenber

# if my_list[j] > my_list[j+2] or (my_list[j] == my_list[j+2] and my_list[j-1] < my_list[j+1]):
# -----------------------------------------vs
# if int(my_list[j]) > int(my_list[j+2]) or (int(my_list[j]) == int(my_list[j+2]) and my_list[j-1] > my_list[j+1]):


# -----------------------what is the difference in both

# in without int if statement --> Here, the roll numbers (marks) are compared as strings, not integers.
                            # This works correctly as long as all numbers have the same number of digits. 
                            # but
                            # if roll numbers differ in length (e.g., "100" vs "78"), 
                            # the comparison fails because string comparison is lexicographical,not numerical.

                            # matlab
                            # string comprasion mai 2 digit hai then 2 digit ka comparision mai he corren=ct hoga

# but in int if statement --> Roll numbers are explicitly converted to integers using int() before 
                            # comparison. This ensures numerical correctness even for numbers of varying lengths.
                            # eg : 78>100  --> correct comparision

