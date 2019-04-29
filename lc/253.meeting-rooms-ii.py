#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (42.73%)
# Total Accepted:    143.3K
# Total Submissions: 335.3K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ts = []
        for il in intervals:
            ts.extend([(il[0], 1), (il[1], -1)])
        ts.sort()

        ans = 0
        cur = 0

        for t in ts:
            if t[1] > 0:
                cur += 1
                ans = max(ans, cur)
            else:
                cur -= 1
        
        return ans
        
