#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (58.02%)
# Total Accepted:    21.5K
# Total Submissions: 37K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# We should return its level order traversal:
# 
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# Note:
# 
# 
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        ans = []
        tmp = []
        dq = collections.deque()
        dq.append(root)
        dq.append('#')
        while len(dq) > 0:
            if dq[0] == '#' and len(dq) == 1:
                if len(tmp) > 0:
                    ans.append(tmp)    
                break
            top = dq[0]
            dq.popleft()
            if top == '#':
                dq.append('#')
                ans.append(tmp)
                tmp = []
                continue
            elif top == None:
                continue
            else:
                tmp.append(top.val)
                for chl in top.children:
                    dq.append(chl)

        return ans
