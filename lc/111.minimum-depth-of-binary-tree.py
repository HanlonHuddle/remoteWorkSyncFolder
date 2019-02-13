#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (34.37%)
# Total Accepted:    255.5K
# Total Submissions: 743.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dq = collections.deque()
        dq.append(root)
        dq.append(None)

        curd = 1

        while len(dq) > 0:
            cur = dq.popleft()
            if not cur and len(dq) > 0:
                curd += 1
                dq.append(None)
            else:
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
                if not cur.left and not cur.right:
                    return curd
        
        return curd
