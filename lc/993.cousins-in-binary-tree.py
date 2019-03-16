#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (53.98%)
# Total Accepted:    6.8K
# Total Submissions: 12.7K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# 
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
# 
# 
# 
# 
# 
# 
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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if x == y:
            return False
        xr = [-2, -1]
        yr = [-2, -1]
        def helper(rt, parent, depth):
            nonlocal xr, yr
            if (xr[0] != -2 and yr[0] != -2) or rt == None:
                return
            if rt.val == x:
                xr[0] = parent
                xr[1] = depth
            if rt.val == y:
                yr[0] = parent
                yr[1] = depth
            helper(rt.left, rt.val, depth+1)
            helper(rt.right, rt.val, depth+1)

        helper(root, 0, -1)
        return xr[1] == yr[1] and xr[0] != yr[0]
