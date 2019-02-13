#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (53.87%)
# Total Accepted:    31.3K
# Total Submissions: 58.1K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        dic = {}
        for i in range(ord('a'), ord('z')+1, 1):
            dic[chr(i)] = chr(i + ord('A') - ord('a'))
            dic[chr(i + ord('A') - ord('a'))] = chr(i)
        
        tans = [[]]
        for c in S:
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
                l = len(tans)
                for i in range(l):
                    ls = tans[i]
                    cpls = ls.copy()
                    ls.append(c)
                    cpls.append(dic[c])
                    tans.append(cpls)
            else:
                for ls in tans:
                    ls.append(c)
        ans = []
        for a in tans:
            ans.append(''.join(a))
        return ans

        
