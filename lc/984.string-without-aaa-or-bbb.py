#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Easy (31.35%)
# Total Accepted:    4.9K
# Total Submissions: 15.6K
# Testcase Example:  '1\n2'
#
# Given two integers A and B, return any string S such that:
# 
# 
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b'
# letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = 4, B = 1
# Output: "aabaa"
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.
# 
#
class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ans = []
        while A > 0 or B > 0:
            na, nb = 0, 0

            if len(ans) == 0:
                if A > B:
                    na = min(2, A)
                else:
                    nb = min(2, B)
            else:
                if ans[-1] == 'a':
                    if A > B:
                        nb = min(1, B)
                    else:
                        nb = min(2, B)
                else:
                    if A > B:
                        na = min(2, A)
                    else:
                        na = min(1, A)
            
            if na == 0 and nb == 0:
                na = A
                nb = B

            ans.extend(['a'] * na)
            ans.extend(['b'] * nb)
            A -= na
            B -= nb
        
        return ''.join(ans)
