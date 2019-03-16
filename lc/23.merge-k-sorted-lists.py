#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (32.86%)
# Total Accepted:    341K
# Total Submissions: 1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hp = []
        if len(lists) < 1:
            return None
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(hp, (lists[i].val, i))
                
        head = ListNode(-1)
        tail = head
        while len(hp) > 0:
            cur = heapq.heappop(hp)    
            tail.next = ListNode(cur[0])
            tail = tail.next
            if lists[cur[1]] != None:
                lists[cur[1]] = lists[cur[1]].next
                if lists[cur[1]] != None:
                    heapq.heappush(hp, (lists[cur[1]].val, cur[1]))
            else:
                pass
        return head.next        
