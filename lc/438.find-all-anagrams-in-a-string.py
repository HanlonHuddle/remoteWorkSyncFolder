#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.02%)
# Total Accepted:    103.7K
# Total Submissions: 287.9K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#
class Solution:
    def findAnagrams(self, s: 'str', p: 'str') -> 'List[int]':
        ans = []
        if len(s) < len(p):
            return ans
        fp = collections.Counter(p)
        hm = collections.defaultdict(int)
        for i in range(len(p)):
            hm[s[i]] += 1
        for i in range(len(s)-len(p)+1):
            flag = True
            for key in fp:
                if fp[key] != hm[key]:
                    flag = False
                    break
            if flag:
                ans.append(i)
            if i < len(s) - len(p):
                hm[s[i]] -= 1
                hm[s[i+len(p)]] += 1
        return ans

        
