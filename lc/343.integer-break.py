#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#
# https://leetcode.com/problems/integer-break/description/
#
# algorithms
# Medium (47.26%)
# Total Accepted:    73.1K
# Total Submissions: 154.8K
# Testcase Example:  '2'
#
# Given a positive integer n, break it into the sum of at least two positive
# integers and maximize the product of those integers. Return the maximum
# product you can get.
# 
# Example 1:
# 
# 
# 
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# 
# Note: You may assume that n is not less than 2 and not larger than 58.
# 
# 
#
class Solution:
    def integerBreak(self, n: 'int') -> 'int':
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n%3 == 0:
            return 3**(n//3)
        elif n%3 == 1:
            return 3**((n//3)-1) * 4
        else:
            return 3**(n//3) * 2
        return ans