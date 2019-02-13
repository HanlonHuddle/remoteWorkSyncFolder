#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (43.95%)
# Total Accepted:    221.5K
# Total Submissions: 502.4K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        ans = [[1]]
        if numRows == 0:
            return []
        while numRows > 1:
            tmp = []
            for i in range(len(ans[-1]) + 1):
                lv = 0 if i == 0 else ans[-1][i-1]
                rv = 0 if i == len(ans[-1]) else ans[-1][i]
                tmp.append(lv + rv)
            ans.append(tmp)
            numRows -= 1
        return ans

