#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Easy (39.32%)
# Total Accepted:    23.6K
# Total Submissions: 59.9K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K. How long will it take for all
# nodes to receive the signal? If it is impossible, return -1.
# 
# Note:
# 
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <=
# 100.
# 
# 
# 
# 
#
class Solution:
    def networkDelayTime(self, times: 'List[List[int]]', N: 'int', K: 'int') -> 'int':
        hm = collections.defaultdict(list)
        for time in times:
            hm[time[0]].append( (time[1], time[2]) )
            if time[1] not in hm:
                hm[time[1]] = []
        ans = -1
        s = set(k)
        
        

        
