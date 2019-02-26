#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.21%)
# Total Accepted:    181.8K
# Total Submissions: 547.3K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[-1][-1] == 1:
            return 0
            
        dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        dp[-1][-1] = 1

        si, sj = len(dp)-1, len(dp[0])-1
        i, j = si, sj
        for i in range(si-1, -1, -1):
            dp[i][j] = dp[i+1][j] if obstacleGrid[i][j] == 0 else 0
        i, j = si, sj
        for j in range(sj-1, -1, -1):
            dp[i][j] = dp[i][j+1] if obstacleGrid[i][j] == 0 else 0
        
        si, sj = len(dp)-2, len(dp[0])-2

        while si >= 0 and sj >= 0:
            i, j = si, sj
            for i in range(si, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1] if obstacleGrid[i][j] == 0 else 0
            i, j = si, sj
            for j in range(sj, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1] if obstacleGrid[i][j] == 0 else 0
            si -= 1
            sj -= 1
                    
        return dp[0][0]
