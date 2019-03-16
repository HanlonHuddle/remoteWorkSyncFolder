#
# @lc app=leetcode id=545 lang=python3
#
# [545] Boundary of Binary Tree
#
# https://leetcode.com/problems/boundary-of-binary-tree/description/
#
# algorithms
# Medium (34.18%)
# Total Accepted:    17.9K
# Total Submissions: 52.2K
# Testcase Example:  '[1,null,2,3,4]'
#
# Given a binary tree, return the values of its boundary in anti-clockwise
# direction starting from root.
# Boundary includes left boundary, leaves, and right boundary in order without
# duplicate nodes. 
# 
# Left boundary is defined as the path from root to the left-most node. Right
# boundary is defined as the path from root to the right-most node. If the root
# doesn't have left subtree or right subtree, then the root itself is left
# boundary or right boundary. Note this definition only applies to the input
# binary tree, and not applies to any subtrees.
# 
# The left-most node is defined as a leaf node you could reach when you always
# firstly travel to the left subtree if exists. If not, travel to the right
# subtree. Repeat until you reach a leaf node.
# 
# The right-most node is also defined by the same way with left and right
# exchanged.
# 
# 
# Example 1
# 
# Input:
# ⁠ 1
# ⁠  \
# ⁠   2
# ⁠  / \
# ⁠ 3   4
# 
# Ouput:
# [1, 3, 4, 2]
# 
# Explanation:
# The root doesn't have left subtree, so the root itself is left boundary.
# The leaves are node 3 and 4.
# The right boundary are node 1,2,4. Note the anti-clockwise direction means
# you should output reversed right boundary.
# So order them in anti-clockwise without duplicates and we have [1,3,4,2].
# 
# 
# 
# 
# Example 2
# 
# Input:
# ⁠   ____1_____
# ⁠  /          \
# ⁠ 2            3
# ⁠/ \          / 
# 4   5        6   
# ⁠  / \      / \
# ⁠ 7   8    9  10  
# ⁠      
# Ouput:
# [1,2,4,7,8,9,10,6,3]
# 
# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to
# definition)
# The leaves are node 4,7,8,9,10.
# The right boundary are node 1,3,6,10. (10 is the right-most node).
# So order them in anti-clockwise without duplicate nodes we have
# [1,2,4,7,8,9,10,6,3].
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
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        ans, cur = [], root
        if cur == None:
            return ans
        if cur.left == None:
            if cur.right != None:
                ans.append(cur.val)
        else:
            while cur != None:
                if cur.left != None:
                    ans.append(cur.val)
                    cur = cur.left
                elif cur.right != None:
                    ans.append(cur.val)
                    cur = cur.right
                else:
                    break
        def helper(rt):
            nonlocal ans
            if rt == None:
                return
            helper(rt.left)
            if rt.left == None and rt.right == None:
                ans.append(rt.val)
            helper(rt.right)
        helper(root)
        ls = []
        cur = root
        if cur.right != None:
            cur = cur.right
            while cur != None:
                if cur.right != None:
                    ls.append(cur.val)
                    cur = cur.right
                elif cur.left != None:
                    ls.append(cur.val)
                    cur = cur.left
                else:
                    break
        if len(ls) > 0:
            ans.extend(ls[::-1])
        return ans
