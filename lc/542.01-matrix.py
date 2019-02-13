#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (34.16%)
# Total Accepted:    33.9K
# Total Submissions: 99.2K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# Example 1: 
# Input:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 
# Example 2: 
# Input:
# 
# 0 0 0
# 0 1 0
# 1 1 1
# 
# Output:
# 
# 0 0 0
# 0 1 0
# 1 2 1
# 
# 
# 
# Note:
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# 
# 
#
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp = None
                for dir in dirs:
                    if 0 <= i+dir[0] < len(matrix) and 0 <= j+dir[1] < len(matrix[0]):
                        tmp = min(tmp, matrix[i+dir[0]][j+dir[1]]) if tmp != None else matrix[i+dir[0]][j+dir[1]]
                matrix[i][j] = tmp+1 if matrix[i][j]!=0 else 0
        
        return matrix
