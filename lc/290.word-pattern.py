#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (34.53%)
# Total Accepted:    131.8K
# Total Submissions: 381.3K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
#
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        ls = str.split(' ')
        if len(pattern) != len(ls):
            return False
        hm = {}
        rhm = {}
        for i, c in enumerate(pattern):
            if c not in hm:
                if ls[i] in rhm:
                    return False
                hm[c] = ls[i]
                rhm[ls[i]] = c
            else:
                if hm[c] != ls[i]:
                    return False
        return True
