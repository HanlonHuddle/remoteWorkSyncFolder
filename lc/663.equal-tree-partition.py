#
# @lc app=leetcode id=663 lang=python3
#
# [663] Equal Tree Partition
#
# https://leetcode.com/problems/equal-tree-partition/description/
#
# algorithms
# Medium (37.57%)
# Total Accepted:    12.4K
# Total Submissions: 33.1K
# Testcase Example:  '[5,10,10,null,null,2,3]'
#
# 
# Given a binary tree with n nodes, your task is to check if it's possible to
# partition the tree to two trees which have the equal sum of values after
# removing exactly one edge on the original tree.
# 
# 
# Example 1:
# 
# Input:     
# ⁠   5
# ⁠  / \
# ⁠ 10 10
# ⁠   /  \
# ⁠  2   3
# 
# Output: True
# Explanation: 
# ⁠   5
# ⁠  / 
# ⁠ 10
# ⁠     
# Sum: 15
# 
# ⁠  10
# ⁠ /  \
# ⁠2    3
# 
# Sum: 15
# 
# 
# 
# 
# Example 2:
# 
# Input:     
# ⁠   1
# ⁠  / \
# ⁠ 2  10
# ⁠   /  \
# ⁠  2   20
# 
# Output: False
# Explanation: You can't split the tree into two trees with equal sum after
# removing exactly one edge on the tree.
# 
# 
# 
# Note:
# 
# The range of tree node value is in the range of [-100000, 100000].
# 1 
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
    def checkEqualTree(self, root: 'TreeNode') -> 'bool':
        hm = collections.defaultdict(int)
        def treeSum(rt):
            nonlocal hm
            if rt == None:
                return 0
            if rt in hm:
                return hm[rt]
            hm[rt] = treeSum(rt.left) + treeSum(rt.right) + rt.val
            return hm[rt]

        tsum = treeSum(root)

        if tsum % 2 != 0:
            return False

        for key in hm:
            if hm[key] == tsum // 2 and key != root:
                return True
        
        return False
