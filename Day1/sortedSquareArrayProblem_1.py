"""
    Question:
    You are given an array of integers in which each subsequent
    value is not less than the previous value. Write a function
    that takes this array as an input and returns a new array
    with the squares of each number sorted in ascending order.

    Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

    Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
    Explanation: After squaring, the array becomes [49,9,4,9,121].
    After sorting, it becomes [4,9,9,49,121].
"""

def square_sort_asc(arr: list):
    """
    This function takes an array of integers and returns a new array with
    the squares of each number, sorted in ascending order.

    - If the array is empty, it returns an empty array.
    - It handles both positive and negative numbers correctly.

    Time Complexity:
    - The time complexity is O(n log n) due to the sorting step after squaring.

    Space Complexity:
    - The space complexity is O(n) for storing the squared values in the new array.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The array of squared numbers sorted in ascending order.
    """
    if len(arr) == 0:
        return arr  # Return the array as is if empty

    new_arr = []  # Initialize an empty array to store squared values
    for num in arr:
        new_arr.append(num * num)  # Square each number and add it to new_arr

    new_arr.sort()  # Sort the array in ascending order

    return new_arr

# Test Cases:
print(square_sort_asc([])) # Test with an empty array, should return []
print(square_sort_asc([3,2,1])) # Test with a sorted array, should return [1,4,9]
print(square_sort_asc([0,5,7])) # Test with a sorted array, should return [0,25,49]
print(square_sort_asc([-7,-3,2,3,11])) # Test with both negative and positive numbers, should return [4,9,9,49,121]
