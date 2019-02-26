#
# @lc app=leetcode id=369 lang=python3
#
# [369] Plus One Linked List
#
# https://leetcode.com/problems/plus-one-linked-list/description/
#
# algorithms
# Medium (55.61%)
# Total Accepted:    31.2K
# Total Submissions: 56.1K
# Testcase Example:  '[1,2,3]'
#
# Given a non-negative integer represented as non-empty a singly linked list of
# digits, plus one to the integer.
# 
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
# 
# The digits are stored such that the most significant digit is at the head of
# the list.
# 
# 
# Example :
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# 
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if head == None:
            return ListNode(1)
        st = []
        cur = head
        while cur.next != None:
            st.append(cur)
            cur = cur.next
        cur.val += 1
        tmpw = 0
        while cur.val > 9 and len(st) > 0:
            cur.val -= 10
            tmpw = 1
            cur = st.pop()
            cur.val += tmpw
            tmpw = 0
        if cur.val > 9:
            nhd = ListNode(cur.val // 10)
            nhd.next = cur
            cur.val = cur.val % 10
            return nhd
        return head