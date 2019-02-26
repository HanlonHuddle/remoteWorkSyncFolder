#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (41.16%)
# Total Accepted:    11.8K
# Total Submissions: 28.7K
# Testcase Example:  '10'
#
# 
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
# 
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x <= y.)
# 
# 
# Example 1:
# 
# Input: N = 10
# Output: 9
# 
# 
# 
# Example 2:
# 
# Input: N = 1234
# Output: 1234
# 
# 
# 
# Example 3:
# 
# Input: N = 332
# Output: 299
# 
# 
# 
# Note:
# N is an integer in the range [0, 10^9].
# 
#
class Solution:
    def monotoneIncreasingDigits(self, N: 'int') -> 'int':
        ns = str(N)
        ans = []
        i = 1
        while i < len(ans):
            if int(ns[i]) >= int (ns[i-1]):
                i += 1
        ans.extend(ns[0:i])
        if i >= len(ans) - 1:
            return int(''.join(ans))
        ans[-1] = str(int(ans[-1])-1)
        ans.extend(['9'] * (len(ans) - i))
        return int(''.join(ans))
