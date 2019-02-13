#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#
# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (28.59%)
# Total Accepted:    48.8K
# Total Submissions: 170.1K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# Design and implement a TwoSum class. It should support the following
# operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
# 
# Example 1:
# 
# 
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# 
# 
# Example 2:
# 
# 
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false
# 
#
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = collections.defaultdict(int)
        
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.hm[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        ans = False
        for n in self.hm:
            if value - n in self.hm:
                if value - n == n and self.hm[n] < 2:
                        continue
                ans = True
        return ans

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
