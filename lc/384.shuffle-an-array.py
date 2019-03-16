#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (49.42%)
# Total Accepted:    68.4K
# Total Submissions: 138.4K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Shuffle a set of numbers without duplicates.
# 
# 
# Example:
# 
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // Shuffle the array [1,2,3] and return its result. Any permutation of
# [1,2,3] must equally likely to be returned.
# solution.shuffle();
# 
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
# 
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
# 
# 
#
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.copy = copy.copy(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.copy

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.nums = copy.copy(self.copy)
        for i in range(len(self.nums)-1, -1, -1):
            j = int(random.random() * i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
