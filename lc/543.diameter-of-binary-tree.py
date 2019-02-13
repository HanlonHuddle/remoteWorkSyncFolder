#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (45.57%)
# Total Accepted:    97.6K
# Total Submissions: 214.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return [0, 0, 1]
            ll, rl, m = 0, 0, 0
            if root.left:
                curl = helper(root.left)
                ll = max(curl[0], curl[1])
                m = max(curl[2], m)
            if root.right:
                curr = helper(root.right)
                rl = max(curr[0], curr[1])
                m = max(curr[2], m)
            return [ll + 1, rl + 1, max(ll + rl + 1, m)]

        return helper(root)[2] - 1
