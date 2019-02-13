#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (45.05%)
# Total Accepted:    201.6K
# Total Submissions: 447.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root == None:
            return ans
        dq = collections.deque()
        dq.append(root)
        dq.append('#')
        tmp = []
        while len(dq) > 0:
            if len(dq) == 1 and dq[0] == '#':
                break
            if dq[0] == '#':
                ans.append(copy.copy(tmp))
                tmp = []
                if len(dq) > 1:
                    dq.append('#')
            elif dq[0] != None:
                tmp.append(dq[0].val)
                dq.append(dq[0].left)
                dq.append(dq[0].right)
            dq.popleft()
        ans.reverse()
        return ans
