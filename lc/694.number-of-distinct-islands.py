#
# @lc app=leetcode id=694 lang=python3
#
# [694] Number of Distinct Islands
#
# https://leetcode.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (49.71%)
# Total Accepted:    21.6K
# Total Submissions: 43.4K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Count the number of distinct islands.  An island is considered to be the same
# as another if and only if one island can be translated (and not rotated or
# reflected) to equal the other.
# 
# Example 1:
# 
# 11000
# 11000
# 00011
# 00011
# 
# Given the above grid map, return 1.
# 
# 
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
# Notice that:
# 
# 11
# 1
# 
# and
# 
# ⁠1
# 11
# 
# are considered different island shapes, because we do not consider reflection
# / rotation.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution:
    def numDistinctIslands(self, grid: 'List[List[int]]') -> 'int':
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0

        shapes = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        seen = set()

        def dfs(i, j, i0, j0):
            nonlocal dirs, shapes, shape, seen
            for dir in dirs:
                ni, nj = i+dir[0], j+dir[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1 and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    shape.add((ni-i0, nj-j0))
                    dfs(ni, nj, i0, j0)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    shape = set()
                    seen.add((i, j))
                    dfs(i, j, i, j)
                    shapes.add(tuple(shape))
        
        return len(shapes)
