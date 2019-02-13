#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (50.29%)
# Total Accepted:    318.6K
# Total Submissions: 633.5K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = None
        c = 0

        for num in nums:
            if c == 0:
                x = num
                c += 1
            else:
                if num != x:
                    c -= 1
                else:
                    c += 1
        
        c = 0

        for num in nums:
            if num == x:
                c += 1
                
        if c > len(nums) / 3:
            return x
        else:
            return None

