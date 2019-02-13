#
# @lc app=leetcode id=276 lang=python
#
# [276] Paint Fence
#
# https://leetcode.com/problems/paint-fence/description/
#
# algorithms
# Easy (35.90%)
# Total Accepted:    39.3K
# Total Submissions: 109.5K
# Testcase Example:  '3\n2'
#
# There is a fence with n posts, each post can be painted with one of the k
# colors.
# 
# You have to paint all the posts such that no more than two adjacent fence
# posts have the same color.
# 
# Return the total number of ways you can paint the fence.
# 
# Note:
# n and k are non-negative integers.
# 
# Example:
# 
# 
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways
# are:
# 
# post1  post2  post3      
# ⁠-----      -----  -----  -----       
# ⁠  1         c1     c1     c2 
# 2         c1     c2     c1 
# 3         c1     c2     c2 
# 4         c2     c1     c1  
# ⁠  5         c2     c1     c2
# 6         c2     c2     c1
# 
# 
#
class Solution(object):
    def __init__(self):
        self.hm = {}
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if (n, k) in self.hm:
            return self.hm[(n, k)]
        if (n <= 0):
            return 1
        if (k <= 0):
            return 0
        if (n == 1):
            return k
        tmp = k*self.numWays(n-1, k-1) + k*self.numWays(n-2, k-1)
        self.hm[(n, k)] = tmp
        return tmp
