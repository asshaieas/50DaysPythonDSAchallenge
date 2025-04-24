# 🔹 First: Accessing and setting elements in an array
# This is a basic operation that takes O(1) time and space complexity,
# even when the array is very large. It's efficient!

arr = [1, 3, 5, 6, 7, 9, 12, 4]
# Accessing the element at index 7 (remember, indexing starts from 0!):
print(arr[7])  # Output: 4

# Modifying the element at index 7:
arr[7] = 5  # Changing the value at index 7 from 4 to 5
print(arr[7])  # Output: 5

# 💡 Tip: Accessing and setting values in arrays is a constant-time operation,
# which makes arrays very efficient for these tasks!

# 🔹 Second: Traversing and searching in an array
# The time complexity for traversing the array is O(n),
# where n is the number of elements. Space complexity is O(1).

arr.reverse()  # Reversing the array
print(arr)  # Output: [5, 12, 9, 7, 6, 5, 3, 1]

# Searching for an element:
print(arr.index(5))  # Output: 0 (Found the first occurrence of 5 at index 0)

# 💡 Tip: If the element you're looking for is near the beginning,
# searching can be quick with O(1) time complexity. But for larger arrays,
# it can take O(n) time.

# 🔹 Third: Copying an array
# Copying an array involves creating a new array. Time and space complexity is O(n).

copyArr = arr.copy()
print(copyArr)  # Output: [5, 12, 9, 7, 6, 5, 3, 1]

# 💡 Tip: Use `.copy()` to avoid modifying the original array when you need a copy!

# 🔹 Fourth: Inserting an element into an array
# Insertion can happen at various positions with different time complexities:
    # - At the beginning: O(n) time (shift all elements)
    # - At the end: O(1) in dynamic arrays (like Python), but O(n) in static arrays (like in C/C++)
    # - In the middle: O(n) time (due to shifting elements)
# Space complexity for insertion is O(1).

arr.insert(4, 5)  # Inserting 5 at index 4
print(arr)  # Output: [5, 12, 9, 7, 5, 6, 5, 3, 1]

# 💡 Tip: In dynamic arrays, inserting at the end is efficient,
# but inserting in the middle or at the beginning can be costly due to shifting elements.

# 🔹 Fifth: Removing elements from an array
# Time complexity depends on the position of the element:
    # - At the beginning: O(n) (shift elements)
    # - At the end: O(1) (no shifting required)
    # - In the middle: O(n) (shift elements)
# Space complexity is O(1).

arr.remove(6)  # Removing the first occurrence of 6
print(arr)  # Output: [5, 12, 9, 7, 5, 5, 3, 1]

arr.remove(5)  # Removing the first occurrence of 5
print(arr)  # Output: [12, 9, 7, 5, 5, 3, 1]

# 💡 Tip: `remove()` only removes the first occurrence of the element.
# If you need to remove all occurrences, consider using a loop or a list comprehension.

