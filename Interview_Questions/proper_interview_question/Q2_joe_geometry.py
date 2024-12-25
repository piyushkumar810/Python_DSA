# joe is developing a geometry analysis tool that takes four angle as input to determine the quadrilateral
# formed by these angles. the programs checks if the angles sum is equal to 360 degree, indicating a potential 
# quadrilateral.
# the tool prompts the user to enter four angles of a quadrilateral and the program should determine whether 
# the angle forms a quadrilateral. once the shape determined , incorporate the break statement.

def check_quadrilateral(angles):
    seperated_angle=angles.split(" ")
    # print(seperated_angle)

    no_of_angles=len(seperated_angle)
    # print(no_of_angles)

    if(no_of_angles==4):
        sum_of_angles=0
        for i in seperated_angle:
            sum_of_angles=sum_of_angles+int(i)
        return sum_of_angles
    
    else:
        return f"your no of entered angle is may be less than or greater then four "

angle=input("input four angles space seperated : ")
angles=check_quadrilateral(angle)
# print(angles)
if(angles==360):
    print(f"sum of all angles are : {angles}")
    print(f"so, your entered angles makes a quadrilateral ")
else:
    print(f"sum of all angles are : {angles}")
    print("so, it is not a quadrilateral")