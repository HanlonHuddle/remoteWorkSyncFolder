#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (36.82%)
# Total Accepted:    111.9K
# Total Submissions: 303.8K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a stack using queues.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# 
# 
# Example:
# 
# 
# MyStack stack = new MyStack();
# 
# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
# 
# 
#
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dq = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.dq.appendleft(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self.dq) - 1):
            self.dq.appendleft(self.dq.pop())
        return self.dq.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for i in range(len(self.dq) - 1):
            self.dq.appendleft(self.dq.pop())
        ans = self.dq.pop()
        self.dq.appendleft(ans)
        return ans

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.dq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
