#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#
# https://leetcode.com/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (64.25%)
# Total Accepted:    64K
# Total Submissions: 99.6K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
# 
# Example:
# 
# 
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
# 
# 
# 
# 
#
class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.dq = collections.deque()
        self.sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.dq) < self.size:
            self.dq.append(val)
            self.sum += val
        else:
            self.sum -= self.dq[0]
            self.dq.popleft()
            self.dq.append(val)
            self.sum += val
        
        return self.sum / len(self.dq)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
