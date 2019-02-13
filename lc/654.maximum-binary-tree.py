#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#
# https://leetcode.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (71.48%)
# Total Accepted:    55.9K
# Total Submissions: 78.3K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 
# Given an integer array with no duplicates. A maximum tree building on this
# array is defined as follow:
# 
# The root is the maximum number in the array. 
# The left subtree is the maximum tree constructed from left part subarray
# divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray
# divided by the maximum number. 
# 
# 
# 
# 
# Construct the maximum tree by the given array and output the root node of
# this tree.
# 
# 
# Example 1:
# 
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    / 
# ⁠    2  0   
# ⁠      \
# ⁠       1
# 
# 
# 
# Note:
# 
# The size of the given array will be in the range [1,1000].
# 
# 
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, l, r):
            print(l, r)
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            else:
                tmax = nums[l]
                maxi = l
                for i in range(l, r+1):
                    if nums[i] > tmax:
                        tmax = nums[i]
                        maxi = i
                curNode = TreeNode(tmax)
                curNode.left = helper(nums, l, maxi-1)
                curNode.right = helper(nums, maxi+1, r)
                return curNode
        
        if not nums:
            return None

        return helper(nums, 0, len(nums)-1)
