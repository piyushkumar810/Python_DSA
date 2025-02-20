# ------------------------------------- no of the persion visible in the queue-----------------------------------------

# Q) suppose no of persions standing in a queue form 0 to n-1 of different heights to find the persion can see how 
    #  many persions who are stnding right to him.

# example:-
'''
input: heights=[10,6,8,5,11,9]

output=[3,1,2,1,1,0]
'''

# ------------code

class Solution:
    def canSeePersons(self, heights):
        # Get the number of persons (elements in the heights list)
        n = len(heights)

        # Initialize the result list with zeros (each person starts with 0 visible persons)
        result = [0] * n

        # Stack to keep track of heights in decreasing order (monotonic decreasing stack)
        stack = []

        # Iterate from right to left (backward iteration)
        for i in range(n - 1, -1, -1):
            height = heights[i]
            visibility = 0  # Count of visible persons from the current person

            # While the stack is not empty and the current height is greater than the stack's top
            while stack and height > stack[-1]:  # stack[-1] will always give top element
                stack.pop()  # Remove the smaller person from the stack
                visibility += 1  # Increase the visibility count
            
            # If the stack is not empty after popping, it means there's a taller person in front
            if stack:
                visibility += 1  # The taller person can also be seen
            
            # Store the visibility count in the result array
            result[i] = visibility

            # Push the current person's height onto the stack
            stack.append(height)

        # Return the final result list
        return result


# Create an instance of the Solution class
sol = Solution()

# Sample input list representing the heights of persons
heights = [10, 6, 8, 5, 11, 9]

# Call the function to compute the number of visible persons for each index
result = sol.canSeePersons(heights)

# Print the result list
print(result)
