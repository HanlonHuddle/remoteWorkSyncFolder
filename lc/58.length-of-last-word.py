#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.12%)
# Total Accepted:    239.8K
# Total Submissions: 746.3K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# Input: "Hello World"
# Output: 5
# 
# 
#
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return 0
        spl = s.split(' ')
        ans, i = 0, len(spl) - 1

        while i >= 0 and ans <= 0:
            ans = max(len(spl[i]), ans)
            i -= 1
        
        return ans
        
