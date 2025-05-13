def sum_of_array(arr):
    # Base case: if the array is empty, return 0
    if len(arr) == 0:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the array
    return arr[0] + sum_of_array(arr[1:])

# Example usage
array = [1, 2, 3, 4, 5]
result = sum_of_array(array)
print("Sum of array:", result)