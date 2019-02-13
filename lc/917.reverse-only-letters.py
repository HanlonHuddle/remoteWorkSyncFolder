#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (55.69%)
# Total Accepted:    12.9K
# Total Submissions: 23.1K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        S = list(S)
        i, j = 0, len(S) - 1
        while i < j:
            while not 'a' <= S[i] <= 'z' and not 'A' <= S[i] <= 'Z' and i < j:
                i += 1
            while not 'a' <= S[j] <= 'z' and not 'A' <= S[j] <= 'Z' and i < j:
                j -= 1
            if i >= j:
                break
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
        return ''.join(S)
