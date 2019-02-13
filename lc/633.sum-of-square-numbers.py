#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.78%)
# Total Accepted:    37.7K
# Total Submissions: 115.1K
# Testcase Example:  '5'
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
# 
# Example 1:
# 
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: False
# 
# 
# 
# 
#
class Solution:
    def judgeSquareSum(self, c: 'int') -> 'bool':
        for i in range(int(math.sqrt(c + 2))):
            isq = i ** 2
            if (c - isq) >= 0 and int(math.sqrt(c - isq)) ** 2 == c - isq:
                return True
        return False