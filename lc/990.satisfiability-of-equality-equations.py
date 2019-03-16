#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (38.19%)
# Total Accepted:    4.4K
# Total Submissions: 11.6K
# Testcase Example:  '["a==b","b!=a"]'
#
# Given an array equations of strings that represent relationships between
# variables, each string equations[i] has length 4 and takes one of two
# different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not
# necessarily different) that represent one-letter variable names.
# 
# Return true if and only if it is possible to assign integers to variable
# names so as to satisfy all the given equations.
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
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.  There is no way to assign the variables to
# satisfy both equations.
# 
# 
# 
# Example 2:
# 
# 
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# 
# 
# 
# Example 3:
# 
# 
# Input: ["a==b","b==c","a==c"]
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: ["a==b","b!=c","c==a"]
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: ["c==c","b==d","x!=z"]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ne = collections.defaultdict(set)
        eq = collections.defaultdict(set)
        dq = collections.deque()
        for equ in equations:
            if "==" in equ:
                lr = equ.split("==")
                eq[lr[0]].add(lr[1])
                eq[lr[1]].add(lr[0])
            else:
                lr = equ.split("!=")
                ne[lr[0]].add(lr[1])
                ne[lr[1]].add(lr[0])

        def confli(w1, w2):
            if w1 == w2:
                return True
            nonlocal eq, dq
            seen = set()
            dq.append(w1)
            while len(dq) > 0:
                cur = dq.popleft()
                for cand in eq[cur]:
                    if cand == w2:
                        return True
                    if cand not in seen:
                        seen.add(cand)
                        dq.append(cand)
            return False

        for key in ne:
            for nkey in ne[key]:
                if confli(nkey, key):
                    return False
        return True
