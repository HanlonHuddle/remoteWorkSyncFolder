#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (36.07%)
# Total Accepted:    174.4K
# Total Submissions: 483K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        hm1, hm2 = {}, {}
        for i in range(len(s)):
            if s[i] in hm1 and t[i] in hm2:
                if hm1[s[i]] != t[i] or hm2[t[i]] != s[i]: return False
            elif s[i] not in hm1 and t[i] not in hm2:
                    hm1[s[i]] = t[i]
                    hm2[t[i]] = s[i]
            else:
                return False
        return True
