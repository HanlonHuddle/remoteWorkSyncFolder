#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (43.03%)
# Total Accepted:    78.9K
# Total Submissions: 183.3K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
# 
# Note:
# 
# 
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest
# to the target.
# 
# 
# Example:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# Output: 4
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root == None:
            return None
        if root.val == target:
            return root.val
        if root.val > target:
            if root.left == None:
                return root.val
            tans = self.closestValue(root.left, target)
            return tans if abs(tans-target) < abs(root.val-target) else root.val
        else:
            if root.right == None:
                return root.val
            tans = self.closestValue(root.right, target)
            return tans if abs(tans-target) < abs(root.val-target) else root.val
