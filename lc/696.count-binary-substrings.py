#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#
# https://leetcode.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (52.02%)
# Total Accepted:    25.7K
# Total Submissions: 49.4K
# Testcase Example:  '"00110"'
#
# Give a string s, count the number of non-empty (contiguous) substrings that
# have the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively. 
# 
# Substrings that occur multiple times are counted the number of times they
# occur.
# 
# Example 1:
# 
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's
# and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of
# times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are
# not grouped together.
# 
# 
# 
# Example 2:
# 
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
# number of consecutive 1's and 0's.
# 
# 
# 
# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.
# 
#
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        if s == None or len(s) < 2:
            return 0
        ans = 0
        ls = []
        while i < len(s) and j < len(s):
            cnt = 0
            while j < len(s) and s[j] == s[i]:
                j += 1
            ls.append(j - i)
            i = j
        ans = 0
        if len(ls) < 2:
            return 0
        for i in range(len(ls) - 1):
            ans += min(ls[i], ls[i+1])
        return ans