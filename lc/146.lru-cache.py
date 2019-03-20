#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (23.90%)
# Total Accepted:    260.1K
# Total Submissions: 1.1M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# 
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
#

class myNode:
    def __init__(self, k, v):
        self.key, self.val = k, v
        self.pre, self.nex = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.head, self.tail = myNode('#', '#'), myNode('#', '#')
        self.head.nex, self.tail.pre = self.tail, self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        self.hm[key].pre.nex = self.hm[key].nex
        self.hm[key].nex.pre = self.hm[key].pre

        self.hm[key].pre = self.tail.pre
        self.hm[key].nex = self.tail
        self.tail.pre.nex = self.hm[key]
        self.tail.pre = self.hm[key]
        
        return self.hm[key].val

    def put(self, key: int, value: int) -> None:
        if self.cap < 1:
            return

        if key in self.hm:
            self.hm[key].val = value
            self.get(key)
            return

        if self.cap <= len(self.hm):
            self.hm.pop(self.head.nex.key)
            self.head.nex.nex.pre = self.head
            self.head.nex = self.head.nex.nex

        self.hm[key] = myNode(key, value)

        self.hm[key].pre = self.tail.pre
        self.hm[key].nex = self.tail
        self.tail.pre.nex = self.hm[key]
        self.tail.pre = self.hm[key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
