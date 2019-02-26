#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (49.01%)
# Total Accepted:    53.7K
# Total Submissions: 109.6K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array of size n, find the minimum number of moves
# required to make all array elements equal, where a move is incrementing n - 1
# elements by 1.
# 
# Example:
# 
# Input:
# [1,2,3]
# 
# Output:
# 3
# 
# Explanation:
# Only three moves are needed (remember each move increments two elements):
# 
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# 
#
class Solution:
    def minMoves(self, nums: 'List[int]') -> 'int':
        if len(nums) <= 1:
            return 0
        ans = 0
        minv = nums[0]
        for num in nums:
            minv = min(minv, num)
        for num in nums:
            ans += num - minv
        return ans
        
