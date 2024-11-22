def func(n):
    i=1
    while((i**2)<n):
        i=i+1
        print("hello")

func(16)

# identify time and space complexity

# 1st iteration ---> i=1    
# 2nd iteration ---> i=2 
# 3rd iteration ---> i=3 
#  .                  .
#  .                  .
#  .                  .
# nth iteration ---> i=k

# if you go for n+1 th iteration means loop break (i^2 >= n) then i=k+1 
# i^2 ~ n
# (k+1)^2 ~ n
# putting sq root both side
# k+1 ~ √n

# k=√n

# so, TC = O(√n)
#     SC = O(1)