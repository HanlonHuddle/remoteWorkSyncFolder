#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (36.99%)
# Total Accepted:    138.5K
# Total Submissions: 374.6K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        ts, fs, ans = 0, 0, 0
        for i in range(1, n + 1):
            tmp = i
            while tmp > 0 and tmp % 10 == 0:
                ans += 1
                tmp //= 10
            while tmp > 0 and tmp % 2 == 0:
                ts += 1
                tmp //= 2
            while tmp > 0 and tmp % 5 == 0:
                fs += 1
                tmp //= 5
        return ans + min(ts, fs)

