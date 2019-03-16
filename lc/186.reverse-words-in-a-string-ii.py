#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#
# https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (36.09%)
# Total Accepted:    60.3K
# Total Submissions: 166.6K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# Given an input string , reverse the string word by word. 
# 
# Example:
# 
# 
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 
# Note: 
# 
# 
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# 
# 
# Follow up: Could you do it in-place without allocating extra space?
# 
#
class Solution:
    def reverseWords(self, str: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        for i in range(len(str)//2):
            str[i], str[len(str) - i - 1] = str[len(str) - i - 1], str[i]
        i, j = 0, 0
        while i <= len(str) and j < len(str):
            if (i == len(str) and j < len(str)) or str[i] == ' ':
                for t in range(j, (i+j)//2):
                    str[t], str[i+j-t-1] = str[i+j-t-1], str[t]
                j = i + 1
            i += 1
        