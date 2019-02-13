#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (68.53%)
# Total Accepted:    16.1K
# Total Submissions: 23.5K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is univalued if every node in the tree has the same value.
# 
# Return true if and only if the given tree is univalued.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,1,1,null,1]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2,5,2]
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].
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
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        if root == None:
            return True
        lta = True if (root.left == None or (root.left.val == root.val and self.isUnivalTree(root.left))) else False
        rta = True if (root.right == None or (root.right.val == root.val and self.isUnivalTree(root.right))) else False
        return lta and rta