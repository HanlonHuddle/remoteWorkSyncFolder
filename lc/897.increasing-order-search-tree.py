#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (59.34%)
# Total Accepted:    14.3K
# Total Submissions: 24.1K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# Given a tree, rearrange the tree in in-order so that the leftmost node in the
# tree is now the root of the tree, and every node has no left child and only 1
# right child.
# 
# 
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 
# ⁠      5
# ⁠     / \
# ⁠   3    6
# ⁠  / \    \
# ⁠ 2   4    8
# /        / \ 
# 1        7   9
# 
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# ⁠1
# \
# 2
# \
# 3
# \
# 4
# \
# 5
# \
# 6
# \
# 7
# \
# 8
# \
# ⁠                9  
# 
# Note:
# 
# 
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.
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
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            if not root:
                return None
            if not root.left and not root.right:
                return [root, root]
            elif not root.left:
                tmpr = helper(root.right)
                root.right = tmpr[0]
                return [root, tmpr[1]]
            elif not root.right:
                tmp = helper(root.left)
                tmp[1].right = root
                root.left = None
                return [tmp[0], root]
            else:
                tmp = helper(root.left)
                tmpr = helper(root.right)
                tmp[1].right = root
                root.left = None
                root.right = tmpr[0]
                return [tmp[0], tmpr[1]]
        
        return helper(root)[0]
