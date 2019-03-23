#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (24.93%)
# Total Accepted:    177.1K
# Total Submissions: 707.3K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if r > l:
                l, r = 0, 0
            elif r == l:
                ans = max(ans, l*2)
        l, r = 0, 0
        for c in s[::-1]:
            if c == ')':
                r += 1
            else:
                l += 1
            if l > r:
                l, r = 0, 0
            elif r == l:
                ans = max(ans, r*2)
        return ans