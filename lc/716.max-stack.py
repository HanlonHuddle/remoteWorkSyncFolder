#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#
# https://leetcode.com/problems/max-stack/description/
#
# algorithms
# Easy (38.78%)
# Total Accepted:    15.3K
# Total Submissions: 39.4K
# Testcase Example:  '["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]\n[[],[5],[1],[5],[],[],[],[],[],[]]'
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
# 
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you
# find more than one maximum elements, only remove the top-most one.
# 
# 
# 
# Example 1:
# 
# MaxStack stack = new MaxStack();
# stack.push(5); 
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# 
# 
# 
# Note:
# 
# -1e7 
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.
# 
# 
#
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.tmp = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.st.append(x)
        if len(self.tmp) == 0:
            self.tmp.append(x)
        else:
            self.tmp.append(max(self.tmp[-1], x))

    def pop(self):
        """
        :rtype: int
        """
        ans = self.top()
        self.st.pop()
        self.tmp.pop()
        return ans

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.tmp[-1]

    def popMax(self):
        """
        :rtype: int
        """
        dq = []
        while self.top() != self.peekMax():
            dq.append(self.pop())
        ans = self.top()
        self.pop()
        while len(dq) > 0:
            self.push(dq[-1])
            dq.pop()
        return ans

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
