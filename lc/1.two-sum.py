#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (40.08%)
# Total Accepted:    1.4M
# Total Submissions: 3.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = collections.defaultdict(list)
        for i, num in enumerate(nums):
            hm[num].append(i)
        for num in nums:
            if num == target - num:
                if len(hm[num]) > 1:
                    return [hm[num][0], hm[num][1]]
            else:
                if (target - num) in hm:
                    return [hm[num][0], hm[target-num][0]]
        return []