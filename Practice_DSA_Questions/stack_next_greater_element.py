# --------------------------------- next greater element (NGE)
nums=[1,0,13,17,20,21,8]
result=[-1]*len(nums)
stack=[]

# print(result)

for i in range(len(nums)-1,-1,-1):
    while(stack and nums[i] >= stack[-1]):
    # while len(stack) > 0 and stack[-1] <= nums[i]:   # you can use this insted of while stack
        stack.pop()

    if len(stack)!=0:
        result[i]=stack[-1]
    stack.append(nums[i])

print(result)