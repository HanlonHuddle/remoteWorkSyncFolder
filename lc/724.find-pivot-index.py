#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
# https://leetcode.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (40.36%)
# Total Accepted:    55K
# Total Submissions: 136.2K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# Given an array of integers nums, write a method that returns the "pivot"
# index of this array.
# 
# We define the pivot index as the index where the sum of the numbers to the
# left of the index is equal to the sum of the numbers to the right of the
# index.
# 
# If no such index exists, we should return -1. If there are multiple pivot
# indexes, you should return the left-most pivot index.
# 
# Example 1:
# 
# 
# Input: 
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the
# sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# nums = [1, 2, 3]
# Output: -1
# Explanation: 
# There is no index that satisfies the conditions in the problem
# statement.
# 
# 
# 
# 
# Note:
# 
# 
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].
# 
# 
# 
# 
#
class Solution:
    def pivotIndex(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums) - 1

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            lp = nums[i-1] if i > 0 else 0
            rp = nums[-1] - nums[i] if i < len(nums)-1 else 0
            if lp == rp:
                return i
        
        return -1