#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#
# https://leetcode.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Easy (35.08%)
# Total Accepted:    10.1K
# Total Submissions: 28.8K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
# 
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
# (Each subgrid is contiguous).
# 
# 
# 
# Example 1:
# 
# 
# Input: [[4,3,8,4],
# ⁠       [9,5,1,9],
# ⁠       [2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
# 
# while this one is not:
# 384
# 519
# 762
# 
# In total, there is only one magic square inside the given grid.
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#
class Solution:
    def numMagicSquaresInside(self, grid: 'List[List[int]]') -> 'int':
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        ans = 0
        def helper(i, j):
            nonlocal grid
            if grid[i+1][j+1] != 5:
                return False
            tsum = [0] * 8
            otn = [0] * 9
            for a in range(3):
                for b in range(3):
                    if (grid[i+a][j+b] < 1) or (grid[i+a][j+b] > 9):
                        return False
                    otn[grid[i+a][j+b]-1] += 1
                    tsum[a] += grid[i+a][j+b]
                    tsum[3+b] += grid[i+a][j+b]
                    if a == b:
                        tsum[6] += grid[i+a][j+b]
                    if a+b == 2:
                        tsum[7] += grid[i+a][j+b]
            for s in tsum:
                if s != 15:
                    return False
            for s in otn:
                if s != 1:
                    return False
            return True

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if helper(i, j):
                    ans += 1

        return ans
