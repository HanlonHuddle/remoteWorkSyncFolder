#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (28.30%)
# Total Accepted:    159.1K
# Total Submissions: 562.3K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        hm = {}
        for i in range(26):
            hm[i] = chr(ord('A') + i)
        ls = []
        while n > 0:
            ls.append(hm[(n-1)%26])
            n = (n-1) // 26
        return ''.join(reversed(ls))