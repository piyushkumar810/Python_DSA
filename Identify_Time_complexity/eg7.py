def func(n):
    i=n
    while(i>1):
        i=int(i/2)
        print("hello")

func(8)

# 1st iteration ---> i=n    ------- n/2^0
# 2nd iteration ---> i=n/2  ------- n/2^1
# 3rd iteration ---> i=n/4  ------- n/2^2
#  .                  .
#  .                  .
#  .                  .
# nth iteration ---> i=n/k-1 ------- n/2^k-1

# if you go for n+1 th iteration means loop break (i<=1) i= n/2^k
# n/2^k ~ 1 => n = 2^k
# 2^k = n
# taking log both side
# log2^k = log n
#  k log2 = log n
#  k=log n

# so, TC= O(log n)
#     SC= O(1)