#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (42.01%)
# Total Accepted:    94.8K
# Total Submissions: 225.4K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = collections.defaultdict(list)
        for i, num in enumerate(nums):
            if i > 0:
                nums[i] += nums[i-1]
            hm[nums[i]].append(i)
        ans = 0
        for i, _sum in enumerate(nums):
            if _sum == k:
                ans += 1
            if _sum + k in hm:
                for j in hm[_sum+k]:
                    if j > i:
                        ans += 1
        return ans

