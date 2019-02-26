#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.07%)
# Total Accepted:    318.8K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        s = s.lower()
        i, j = 0, len(s) - 1
        alpn = [str(i) for i in range(10)]
        alpn.extend([chr(i) for i in range(ord('a'), ord('z')+1)])
        alpn = set(alpn)
        
        while i < j:
            while i < len(s) and (s[i] not in alpn):
                i += 1
            while j >= 0 and (s[j] not in alpn):
                j -= 1
            if j >= 0 and i < len(s) and s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
