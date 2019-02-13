#
# @lc app=leetcode id=479 lang=python3
#
# [479] Largest Palindrome Product
#
# https://leetcode.com/problems/largest-palindrome-product/description/
#
# algorithms
# Easy (26.49%)
# Total Accepted:    13.5K
# Total Submissions: 50.9K
# Testcase Example:  '1'
#
# Find the largest palindrome made from the product of two n-digit numbers.
# ⁠Since the result could be very large, you should return the largest
# palindrome mod 1337.
# 
# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
# 
# 
# 
# 
# Note:
# The range of n is [1,8].
# 
# 
#
class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
    if n < 2:
        return 
    i = 10 ** n - 1
    j = i
    while i > 9 and j > 9