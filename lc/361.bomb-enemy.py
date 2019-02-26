#
# @lc app=leetcode id=361 lang=python3
#
# [361] Bomb Enemy
#
# https://leetcode.com/problems/bomb-enemy/description/
#
# algorithms
# Medium (42.33%)
# Total Accepted:    30.9K
# Total Submissions: 73K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
# (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted
# point until it hits the wall since the wall is too strong to be destroyed.
# Note: You can only put the bomb at an empty cell.
# 
# Example:
# 
# 
# 
# Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3 
# Explanation: For the given grid,
# 
# 0 E 0 0 
# E 0 W E 
# 0 E 0 0
# 
# Placing a bomb at (1,1) kills 3 enemies.
# 
# 
#
class Solution:
    def maxKilledEnemies(self, grid: 'List[List[str]]') -> 'int':
        if len(grid) <= 0 or len(grid[0]) <= 0:
            return 0
        hmx = [[[0 for i in range(4)] for j in range(len(grid[0]))] for k in range(len(grid))]
        for i, row in enumerate(grid):
            lt, rt = 0, 0
            for j in range(len(row)):
                if grid[i][j] == '0':
                    hmx[i][j][0] = lt
                elif grid[i][j] == 'E':
                    lt += 1
                else:
                    lt = 0
                
                if grid[i][len(row)-j-1] == '0':
                    hmx[i][len(row)-j-1][1] = rt
                elif grid[i][len(row)-j-1] == 'E':
                    rt += 1
                else:
                    rt = 0
        
        for j in range(len(grid[0])):
            ut, bt = 0, 0
            for i in range(len(grid)):
                if grid[i][j] == '0':
                    hmx[i][j][2] = ut
                elif grid[i][j] == 'E':
                    ut += 1
                else:
                    ut = 0
                
                if grid[len(grid)-i-1][j] == '0':
                    hmx[len(grid)-i-1][j][3] = bt
                elif grid[len(grid)-i-1][j] == 'E':
                    bt += 1
                else:
                    bt = 0
        ans = 0
        for row in hmx:
            for cell in row:
                ans = max(ans, sum(cell))
        
        return ans
                    
