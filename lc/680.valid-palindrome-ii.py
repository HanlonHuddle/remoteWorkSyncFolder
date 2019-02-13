#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (33.46%)
# Total Accepted:    57.2K
# Total Submissions: 170.9K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(s, chance, i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                elif chance > 0:
                    return helper(s, 0, i+1, j) or helper(s, 0, i, j-1)
                else:
                    return False
            return True
        return helper(s, 1, 0, len(s) - 1)
