#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (37.26%)
# Total Accepted:    263.3K
# Total Submissions: 706K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 0
        tans = []
        tmp = '0'
        while i < len(a) or i < len(b):
            ac = a[len(a)-1-i] if i < len(a) else '0'
            bc = b[len(b)-1-i] if i < len(b) else '0'
            if ac == '0' and bc == '0':
                if tmp == '0':
                    tans.append('0')
                    tmp = '0'
                else:
                    tans.append('1')
                    tmp = '0'
            elif ac == '1' and bc == '1':
                if tmp == '0':
                    tans.append('0')
                    tmp = '1'
                else:
                    tans.append('1')
                    tmp = '1'
            else:
                if tmp == '0':
                    tans.append('1')
                    tmp = '0'
                else:
                    tans.append('0')
                    tmp = '1'
            i += 1
        if tmp == '1':
            tans.append(tmp)
        tans.reverse()
        return str(int(''.join(tans)))
