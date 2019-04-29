#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (42.76%)
# Total Accepted:    274.2K
# Total Submissions: 641.1K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#
class Solution:
    def findMin(self, nums: List[int]) -> int:

        def helper(i, j):
            nonlocal nums
            if i == j:
                return None
            if j <= i + 2:
                return min(nums[i:j])
            if nums[j-1] > nums[i]:
                return nums[i]
            mid = (i+j)//2
            if nums[mid] > nums[i]:
                return helper(mid, j)
            else:
                return helper(i, mid+1)

        return helper(0, len(nums))
