#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (46.29%)
# Total Accepted:    258.7K
# Total Submissions: 558.6K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for j in range(n)] for i in range(m)]
        for i in range(0,len(grid)):
            grid[i][0] = 1
        for j in range(0,len(grid[0])):
            grid[0][j] = 1
        ni, nj = 1, 1
        while ni < m or nj < n:
            if nj < n:
                for i in range(ni, m):
                    grid[i][nj] = grid[i-1][nj] + grid[i][ni-1]
            if ni < m:
                for j in range(nj, n):
                    grid[ni][j] = grid[ni-1][j] + grid[ni][j-1]
            ni += 1
            nj += 1
        return grid[-1][-1]