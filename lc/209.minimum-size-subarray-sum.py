#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (34.58%)
# Total Accepted:    171.4K
# Total Submissions: 495.4K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j = 0, 0
        cursum = 0
        if s < 1 or len(nums) < 1:
            return 0
        if sum(nums) < s:
            return 0
        ans = len(nums)
        while j < len(nums):
            while cursum < s and j < len(nums):
                cursum += nums[j]
                j += 1
            if j <= len(nums):
                ans = min(ans, j-i)
            while cursum >= s and i < j:
                ans = min(ans, j-i)
                cursum -= nums[i]
                i += 1
        return ans

