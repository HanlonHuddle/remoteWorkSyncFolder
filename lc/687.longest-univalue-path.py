#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (33.19%)
# Total Accepted:    48.9K
# Total Submissions: 147.3K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# Note: The length of path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input:
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# 
# 
# Output:
# 
# 2
# 
# 
# 
# Note:
# The given binary tree has not more than 10000 nodes.  The height of the tree
# is not more than 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(rt):
            if rt == None:
                return 0
            la, ra = 0, 0
            if rt.left != None and rt.left.val == rt.val:
                la = 1 + helper(rt.left)
            if rt.right != None and rt.right.val == rt.val:
                ra = 1 + helper(rt.right)
            return max(la, ra, 1)

        if root == None or (root.left == None and root.right == None):
            return 0

        snnl = 0 if (root.left == None or root.left.val != root.val) else helper(root.left)
        snnr = 0 if (root.right == None or root.right.val != root.val) else helper(root.right)

        return max(snnl + snnr, self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))