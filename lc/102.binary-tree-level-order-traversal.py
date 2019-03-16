#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (47.07%)
# Total Accepted:    343.5K
# Total Submissions: 726.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
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
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        dq = collections.deque()
        if root == None:
            return ans
        dq.append(root)
        dq.append('#')
        tmp = []
        while len(dq) > 0:
            curNode = dq.popleft()
            if curNode !='#':
                tmp.append(curNode.val)
                if curNode.left != None:
                    dq.append(curNode.left)
                if curNode.right != None:
                    dq.append(curNode.right)
            else:
                ans.append(tmp)
                tmp = []
                if len(dq) > 0:
                    dq.append('#')
        return ans
