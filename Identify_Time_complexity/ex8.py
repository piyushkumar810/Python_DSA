def func(n):
    i=2
    while(i<n):
        i=i*i
        print("hello")

func(16)

# 1st iteration ---> i=2                 ------- 2^1          ------------ (2^1)^0
# 2nd iteration ---> i=4                 ------- 2^2          ------------ (2^2)^1
# 3rd iteration ---> i=16                ------- (2^2)^2      ------------ (2^2)^2
# 4th iteration ---> i=16^2              ------- ((2^2)^2)^2  ------------ (2^2)^3
# 5th iteration ---> i=(((2^2)^2)^2)^2   --------------------------------- (2^2)^4
#  .                  .
#  .                  .
#  .                  .
# nth iteration ---------------------------------------------------------- (2^2)^k-1

# for n+1 th term the loop will break now, (i>=n) then , i=(2^2)^k
#                                    (2^2)^k-1 ~ n
#                                    taking log both side
#                                    log(2^2)^k = log n
#                                    2^k log 2 = log n
#                                    here log 2 base 2 =1 
#                                     2^k = log n
#                                    again taking log both side
#                                    log2^k = log(log n)
#                                    k log2 = log(log n)
#                                    here log 2 base 2 =1 
#                                    k= log(log n)

# so, TC = O(log(log n))
#     SC = O(1)