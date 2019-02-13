#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (57.14%)
# Total Accepted:    64.4K
# Total Submissions: 112.7K
# Testcase Example:  '[3,9,20,15,7]'
#
# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.
# 
# Example 1:
# 
# Input:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
# 2 is 11. Hence return [3, 14.5, 11].
# 
# 
# 
# Note:
# 
# The range of node's value is in the range of 32-bit signed integer.
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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return root
        dq = collections.deque()
        dq.append(root)
        dum = TreeNode('d')
        dq.append(dum)
        ans = []
        tcnt = 0
        ttol = 0
        while dq:
            cur = dq.popleft()
            if cur != dum:
                tcnt += cur.val
                ttol += 1
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            else:
                ans.append(tcnt / ttol)
                tcnt, ttol = 0, 0
                if dq:
                    dq.append(dum)
        return ans