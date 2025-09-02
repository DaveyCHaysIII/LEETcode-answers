"""
1. Two-Sum:

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []


"""
Hard parts: re-learning python

Strategy: for every number of nums, check every subsequent number
to see if it adds up to target

Answer: middle of the road, simplest, brute force

Time Complexity: 0N^2

Better solution: use hash map (add a data structure)

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []

"""


