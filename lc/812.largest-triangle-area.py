#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#
# https://leetcode.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (53.95%)
# Total Accepted:    10.8K
# Total Submissions: 20.1K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# You have a list of points in the plane. Return the area of the largest
# triangle that can be formed by any 3 of the points.
# 
# 
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the
# largest.
# 
# 
# 
# 
# Notes: 
# 
# 
# 3 <= points.length <= 50.
# No points will be duplicated.
# -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.
# 
# 
# 
# 
#
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        if len(points) < 3:
            return 0

        def area(p1, p2, p3):
            return abs((p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0]))/2

        ans = 0

        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for x in range(j + 1, len(points)):
                    ans = max(ans, area(points[i], points[j], points[x]))
        
        return ans
