#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (27.05%)
# Total Accepted:    154.3K
# Total Submissions: 570.3K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#
import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mlen = functools.reduce((lambda a, b: max(a, len(b))), wordDict, 0)
        wd = set(wordDict)
        hm = collections.defaultdict(list)
        hm[-1] = [[]]
        dq = collections.deque([-1])

        while len(dq) > 0:
            i = dq.popleft()
            for j in range(1, mlen+1):
                if s[i+1:i+j+1] in wd:
                    if i+j not in hm:
                        dq.append(i+j)
                    for pre in hm[i]:
                        nlist = pre.copy()
                        nlist.append(s[i+1:i+j+1])
                        hm[i+j].append(nlist)
                        
        return list(map(lambda x:' '.join(x), hm[len(s)-1]))