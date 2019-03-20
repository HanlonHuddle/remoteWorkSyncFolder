#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (36.71%)
# Total Accepted:    194.2K
# Total Submissions: 525.6K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = collections.defaultdict(int)
        outSet = collections.defaultdict(set)
        allCous = set()
        for preq in prerequisites:
            allCous.add(preq[0])
            allCous.add(preq[1])
            if preq[0] == preq[1]:
                return False
            if preq[1] not in outSet[preq[0]]:
                outSet[preq[0]].add(preq[1])
                inDegree[preq[1]] += 1
        dq = collections.deque()
        for node in allCous:
            if inDegree[node] == 0:
                dq.append(node)
        while len(dq) > 0:
            cur = dq.popleft()
            allCous.remove(cur)
            for outc in outSet[cur]:
                inDegree[outc] -= 1
                if inDegree[outc] == 0 and outc in allCous:
                    dq.append(outc)
        return len(allCous) == 0
