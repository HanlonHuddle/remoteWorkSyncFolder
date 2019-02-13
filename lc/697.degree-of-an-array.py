#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (48.86%)
# Total Accepted:    40.2K
# Total Submissions: 82.3K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
# 
# Example 1:
# 
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,2,3,1,4,2]
# Output: 6
# 
# 
# 
# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
# 
#
class Solution:
    def findShortestSubArray(self, nums: 'List[int]') -> 'int':
        hm = collections.defaultdict(list)
        m = 0
        for i, num in enumerate(nums):
            if num not in hm:
                hm[num].extend([i, i, 1])
            else:
                hm[num][1] = i
                hm[num][2] += 1
                m = max(m, hm[num][2])
        ans = len(nums)
        for key in hm:
            if hm[key][2] >= m:
                ans = min(ans, hm[key][1] - hm[key][0] + 1)
        return ans
