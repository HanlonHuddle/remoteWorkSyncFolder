#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (29.20%)
# Total Accepted:    159.1K
# Total Submissions: 545K
# Testcase Example:  '    43261596 (00000010100101000001111010011100)'
#
# Reverse bits of a given 32 bits unsigned integer.
# 
# Example:
# 
# 
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as
# 00000010100101000001111010011100, 
# return 964176192 represented in binary as 00111001011110000010100101000000.
# 
# 
# Follow up:
# If this function is called many times, how would you optimize it?
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        cnt = 32
        while cnt > 0:
            ans += 1 & n
            if n > 0:
                n >>= 1
            cnt -= 1
            if cnt > 0:
                ans <<= 1
        return ans