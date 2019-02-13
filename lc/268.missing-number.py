#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (46.58%)
# Total Accepted:    221.3K
# Total Submissions: 474.8K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(len(nums)+1)
        for i in range(len(nums)):
            while 0 <= nums[i] and nums[i] < len(nums) and nums[i] != i:
                n = nums[i]
                nums[i], nums[n] = nums[n], nums[i]
        for i, n in enumerate(nums):
            if i != n:
                return i
        