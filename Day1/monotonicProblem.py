class Solution(object):
    def isMonotonic(self, nums):
        """
        Function to check if an array is monotonic (either non-increasing or non-decreasing).

        :type nums: List[int]  # Input list of integers
        :rtype: bool  # Returns True if the array is monotonic, False otherwise

        Example:
        1. print(isMonotonic([1, 2, 3]))  # True (increasing)
        2. print(isMonotonic([3, 2, 1]))  # True (decreasing)
        3. print(isMonotonic([1, 2, 3, 2, 1]))  # False (not monotonic)

        Time Complexity: O(n) # We iterate through the list once, where n is the number of elements.
        Space Complexity: O(1) # We use a constant amount of space (only two flags).
        """

        # If the list has 0 or 1 an element, it's trivially monotonic
        if len(nums) <= 1:
            return True

        # Flags to track if the array is increasing or decreasing
        is_increasing, is_decreasing = False, False

        # Traverse the array to check for monotonicity
        for i in range(len(nums) - 1):
            # If the current number is less than the next, it's increasing
            if nums[i] < nums[i + 1]:
                is_increasing = True
            # If the current number is greater than the next, it's decreasing
            elif nums[i] > nums[i + 1]:
                is_decreasing = True

        # If the array is both increasing and decreasing, it's not monotonic
        return not (is_increasing and is_decreasing)


# Create an instance of the Solution class
solution = Solution()

# Test Cases
print(solution.isMonotonic([1, 2, 3]))  # Returns: True (Increasing)
print(solution.isMonotonic([3, 2, 1]))  # Returns: True (Decreasing)
print(solution.isMonotonic([1, 2, 3, 2, 1]))  # Returns: False (Not monotonic)
print(solution.isMonotonic([]))  # Returns: True (Empty)
print(solution.isMonotonic([1])) # Returns: True (One element)
print(solution.isMonotonic([1,2,2]))  # Returns: True (Stile Increasing)
