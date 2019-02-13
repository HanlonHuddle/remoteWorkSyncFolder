#
# @lc app=leetcode id=593 lang=python
#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (39.93%)
# Total Accepted:    16.4K
# Total Submissions: 41K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space, return whether the four
# points could construct a square.
# 
# The coordinate (x,y) of a point is represented by an integer array with two
# integers.
# 
# Example:
# 
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# 
# 
# 
# ⁠Note: 
# 
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
# Input points have no order.
# 
# 
#
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        ls = []
        ls.append((p1[0], p1[1]))
        ls.append((p2[0], p2[1]))
        ls.append((p3[0], p3[1]))
        ls.append((p4[0], p4[1]))
        ls.sort(key = lambda x : (x[0], x[1]));

        ax = ls[1][0] - ls[0][0]
        ay = ls[1][1] - ls[0][1]

        bx = ls[2][0] - ls[0][0]
        by = ls[2][1] - ls[0][1]

        cx = ls[1][0] - ls[3][0]
        cy = ls[1][1] - ls[3][1]

        dx = ls[2][0] - ls[3][0]
        dy = ls[2][1] - ls[3][1]

        return (ls[0] != ls[3]) and (ax*bx + ay*by == 0) and (cx*dx + cy*dy == 0) and (ax**2+ay**2 == bx**2+by**2) and (cx**2+cy**2 == dx**2+dy**2)
        
