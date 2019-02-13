#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (42.73%)
# Total Accepted:    31.8K
# Total Submissions: 74.4K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmonious array is an array where the difference between its
# maximum value and its minimum value is exactly 1.
# 
# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.
# 
# Example 1:
# 
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 
# 
# 
# Note:
# The length of the input array will not exceed 20,000.
# 
# 
# 
#
class Solution:
    def findLHS(self, nums: 'List[int]') -> 'int':
        hm = collections.defaultdict(int)
        for num in nums:
            hm[num] += 1
        ans = 0
        for key in hm:
            if (key - 1) in hm and (key + 1) in hm:
                ans = max(ans, hm[key-1] + hm[key], hm[key] + hm[key+1])
            elif (key - 1) in hm:
                ans = max(ans, hm[key-1] + hm[key])
            elif (key + 1) in hm:
                ans = max(ans, hm[key] + hm[key+1])
            
        return ans
