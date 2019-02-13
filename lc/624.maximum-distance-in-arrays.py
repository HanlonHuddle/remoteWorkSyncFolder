#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#
# https://leetcode.com/problems/maximum-distance-in-arrays/description/
#
# algorithms
# Easy (36.57%)
# Total Accepted:    13.5K
# Total Submissions: 36.9K
# Testcase Example:  '[[1,2,3],[4,5],[1,2,3]]'
#
# 
# Given m arrays, and each array is sorted in ascending order. Now you can pick
# up two integers from two different arrays (each array picks one) and
# calculate the distance. We define the distance between two integers a and b
# to be their absolute difference |a-b|. Your task is to find the maximum
# distance.
# 
# 
# Example 1:
# 
# Input: 
# [[1,2,3],
# ⁠[4,5],
# ⁠[1,2,3]]
# Output: 4
# Explanation: 
# One way to reach the maximum distance 4 is to pick 1 in the first or third
# array and pick 5 in the second array.
# 
# 
# 
# Note:
# 
# Each given array will have at least 1 number. There will be at least two
# non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of
# [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].
# 
# 
#
class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        lss = []
        lsl = []
        for i, arr in enumerate(arrays):
            if arr != None and len(arr) > 0:
                lss.append((arr[0], i))
                lsl.append((-arr[-1], i))
        lss.sort()
        lsl.sort()

        i, j = 0, 0
        while i < len(lss) and j < len(lsl) and lss[i][1] == lsl[j][1]:
            if i+1 >= len(lss):
                j += 1
            if j+1 >= len(lsl):
                i += 1
            if (lss[i+1][0] + lsl[j][0]) < (lss[i][0] + lsl[j+1][0]):
                i += 1
            else:
                j += 1

        return - lss[i][0] - lsl[j][0]

        

