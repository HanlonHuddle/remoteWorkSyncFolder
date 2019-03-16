#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.57%)
# Total Accepted:    5.5K
# Total Submissions: 11.8K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
# 
#
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rot = 0, 0
        dq = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rot += 1
                    dq.append((i, j))
        if fresh == 0:
            return 0
        if rot == 0:
            return -1
        ans = 0
        dq.append('#')
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while len(dq) > 0:
            cur = dq.popleft()
            if cur == '#':
                if len(dq) > 0:
                    dq.append('#')
                    ans += 1
                    continue
                else:
                    break
            for dir in dirs:
                ni, nj = cur[0]+dir[0], cur[1]+dir[1]
                if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    dq.append((ni, nj))
        
        if fresh == 0:
            return ans
        else:
            return -1
