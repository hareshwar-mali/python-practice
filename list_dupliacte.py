# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3

def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == len(set(nums)):
        return False
    else:
        return True

a = contains_duplicate([1,2,3,1])

print(a)