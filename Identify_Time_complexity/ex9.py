def funC(n):
    i=1
    s=1

    while(s<n):
        i +=1
        s=s+i
        print("hello")

# identify time and space complexity

# directly final solution 
#  s=1+2+3+4+ ... +k
# sum of n natural number
# k(k+1)/2 ~ n
# k^2 + k ~ 2n
# ignoring all lower order

# k^2 ~ 2n
# k ~ √2n
# k = √n

# so, 

# TC = O(√n)
# SC = O(1)