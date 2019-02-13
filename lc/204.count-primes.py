#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (27.80%)
# Total Accepted:    205K
# Total Submissions: 735.4K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
#
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        ls = [1] * n
        ls[0], ls[1] = 0, 0
        for i in range(2, n):
            if ls[i] == 1:
                tmp = i*2
                while tmp < n:
                    ls[tmp] = 0
                    tmp += i
        return sum(ls)