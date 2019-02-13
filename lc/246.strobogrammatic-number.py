#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (41.20%)
# Total Accepted:    44.7K
# Total Submissions: 108.5K
# Testcase Example:  '"69"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
# 
# Example 1:
# 
# 
# Input:  "69"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:  "88"
# Output: true
# 
# Example 3:
# 
# 
# Input:  "962"
# Output: false
# 
#
class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return True

        hm = {}
        hm['0'] = '0'
        hm['1'] = '1'
        hm['6'] = '9'
        hm['9'] = '6'
        hm['8'] = '8'
        for i in range((len(num) + 1) // 2):
            if num[i] not in hm:
                return False
            if hm[num[i]] != num[len(num) - 1 - i]:
                return False
        return True    
