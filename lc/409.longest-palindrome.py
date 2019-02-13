#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (46.78%)
# Total Accepted:    80.7K
# Total Submissions: 172.4K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hm = collections.defaultdict(int)
        for c in s:
            hm[c] += 1
        sig = 0
        tans = 0
        for k in hm:
            if hm[k] % 2 == 0:
                tans += hm[k]
            else:
                tans += hm[k] - 1
                sig = 1
        return tans + sig
        
