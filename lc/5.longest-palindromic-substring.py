#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.32%)
# Total Accepted:    466.2K
# Total Submissions: 1.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        mxl = 0
        ai, aj = 0, 0
        for i in range(len(s)):
            j = 0
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                j += 1
            j -= 1
            if mxl < j * 2 + 1:
                mxl = j * 2 + 1
                ai, aj = i-j, i+j
            j = 0
            while i-j >=0 and i+1+j < len(s) and s[i-j] == s[i+1+j]:
                j += 1
            j -= 1
            if mxl < j * 2 + 2:
                mxl = j * 2 + 2
                ai, aj = i-j, i+j+1
        return s[ai:aj+1]
        
