#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.88%)
# Total Accepted:    104.4K
# Total Submissions: 261.6K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#
class Solution:
    def isPowerOfFour(self, num: 'int') -> 'bool':
        while num > 1:
            if num % 4 != 0:
                return False
            num //= 4
        return num == 1
        
