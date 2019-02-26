#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (46.50%)
# Total Accepted:    150.3K
# Total Submissions: 323.1K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dq = collections.deque()
        dq.append(root)
        dq.append('#')
        ans = []
        while len(dq) > 0 and dq[0] != '#':
            cur = dq.popleft()
            if cur == None:
                continue
            if cur.left != None:
                dq.append(cur.left)
            if cur.right != None:
                dq.append(cur.right)
            if dq[0] == '#':
                ans.append(cur.val)
                dq.popleft()
                dq.append('#')
        return ans
