#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (44.44%)
# Total Accepted:    37K
# Total Submissions: 83.3K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
# 
# Example 1:
# 
# Input: 100
# Output: "202"
# 
# 
# 
# Example 2:
# 
# Input: -7
# Output: "-10"
# 
# 
# 
# Note:
# The input will be in range of [-1e7, 1e7].
# 
#
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0 :
            return '0'

        ns = False if num >= 0 else True

        num = abs(num)

        ls = []
        
        while num > 0:
            ls.append(str(num % 7))
            num //= 7

        return ('-' if ns else '') + ''.join(reversed(ls))
