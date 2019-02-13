#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (56.79%)
# Total Accepted:    33.5K
# Total Submissions: 58.9K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# 
# 
# 
# Example 2:
# 
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# 
# 
# 
# Example 3:
# 
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# 
# 
# 
# Example 4:
# 
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
# 
# 
#
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        if n < 2:
            return True
        last = n & 1
        n >>= 1
        while n > 0:
            if not last ^ (n & 1):
                return False
            last = n & 1
            n >>= 1
        return True
