#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#
# https://leetcode.com/problems/complex-number-multiplication/description/
#
# algorithms
# Medium (65.00%)
# Total Accepted:    33.9K
# Total Submissions: 52.2K
# Testcase Example:  '"1+1i"\n"1+1i"'
#
# 
# Given two strings representing two complex numbers.
# 
# 
# You need to return a string representing their multiplication. Note i2 = -1
# according to the definition.
# 
# 
# Example 1:
# 
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it
# to the form of 0+2i.
# 
# 
# 
# Example 2:
# 
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert
# it to the form of 0+-2i.
# 
# 
# 
# Note:
# 
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and
# b will both belong to the range of [-100, 100]. And the output should be also
# in this form.
# 
# 
#
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        als, bls = a.split('+'), b.split('+')
        ar, ai = int(als[0]), 0 if len(als) < 2 else int(als[1][0:-1])
        br, bi = int(bls[0]), 0 if len(bls) < 2 else int(bls[1][0:-1])

        ansr = ar*br - ai*bi
        ansi = ar*bi + ai*br
        return str(ansr)+'+'+str(ansi)+'i'
