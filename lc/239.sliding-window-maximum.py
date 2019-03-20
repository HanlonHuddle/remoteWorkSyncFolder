#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (37.13%)
# Total Accepted:    141.6K
# Total Submissions: 379.9K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        if len(nums) < max(1, k):
            return ans

        dq = collections.deque()

        for i in range(len(nums)):
            if i > k-1 and nums[i-k] == dq[0]:
                dq.popleft()
            if len(dq) < 1:
                dq.append(nums[i])
            else:
                if nums[i] > dq[0]:
                    dq.clear()
                else:
                    while dq[-1] < nums[i]:
                        dq.pop()
                dq.append(nums[i])
            if i >= k-1:
                ans.append(dq[0])
        return ans
