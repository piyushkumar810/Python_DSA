# Q1 -> 
#    Ragav is working as a quality control  inspector at a factory that produces digital combination lock.
# each lock is programmed with four digit code, and ragav's job is to ensure that the codes are easy to
# remember. to do this he checks if the digits of the codes are stricitly descending order , as this 
# pattern is found to be more intuitive for the users.
#    To automate this process , ragav dicided to write a pyhton program that reads four-digit code and 
# determines if its digits are stricitly descending order. if the digits are in correct order , the 
# program should print "Yes"; otherwise the program should print "No" .

# ------------------------------ans
def security_lock(code):
    code_in_list=code.split(" ")
    print(code_in_list)

code=input("enter four digit security pin : ")
result=security_lock(code)
