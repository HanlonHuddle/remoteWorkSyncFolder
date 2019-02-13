#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (50.82%)
# Total Accepted:    459.9K
# Total Submissions: 904.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = None

        def helper(h):
            if h == None or h.next == None:
                ans = h
                return h
            tail = helper(h.next)
            tail.next = h
            h.next = None
            return h
            
        helper(head)
        return ans