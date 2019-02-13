#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (39.17%)
# Total Accepted:    18.9K
# Total Submissions: 48.1K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# In a row of seats, 1 represents a person sitting in that seat, and 0
# represents that the seat is empty. 
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized. 
# 
# Return that maximum distance to closest person.
# 
# 
# Example 1:
# 
# 
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has
# distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# 
# Example 2:
# 
# 
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# 
# 
# Note:
# 
# 
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
# 
# 
# 
# 
#
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ls = [0] * len(seats)
        lmi = None
        for i, s in enumerate(seats):
            if s == 0:
                ls[i] = lmi
            else:
                ls[i] = i
                lmi = i
        rmi = len(seats) * 2
        ans = 0
        for i in range(len(seats)-1, -1, -1):
            s = seats[i]
            if s == 0:
                if ls[i] != None and rmi != None:
                    ans = max(min(rmi - i, i - ls[i]), ans)
                elif ls[i] != None:
                    ans = max(i - ls[i], ans)
                elif rmi != None:
                    ans = max(rmi - i, ans)
                else:
                    ans = max(ans, len(seats))
            else:
                rmi = i
        return ans