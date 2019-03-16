#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#
# https://leetcode.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (55.46%)
# Total Accepted:    9K
# Total Submissions: 16.2K
# Testcase Example:  '[[2]]'
#
# On a N * N grid, we place some 1 * 1 * 1 cubes.
# 
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid
# cell (i, j).
# 
# Return the total surface area of the resulting shapes.
# 
# 
# 
# 
# 
# 
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
# Input: [[2]]
# Output: 10
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[3,4]]
# Output: 34
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,0],[0,2]]
# Output: 16
# 
# 
# 
# Example 4:
# 
# 
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
# 
# 
# 
# Example 5:
# 
# 
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                trs = 0
                for dir in dirs:
                    ni, nj = i+dir[0], j+dir[1]
                    if 0<=ni<len(grid) and 0<=nj<len(grid[0]):
                        trs += min(grid[ni][nj], grid[i][j])
                ans += 4*grid[i][j] - trs + 2 if grid[i][j] > 0 else 0 
        return ans
