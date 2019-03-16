#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (16.85%)
# Total Accepted:    109.2K
# Total Submissions: 646.6K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
# 
# 
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# Example 1:
# 
# 
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# Output: []
# 
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 
# 
# 
# 
# 
#
class Solution:
    def findLadders(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'List[List[str]]':
        hm = collections.defaultdict(set)
        def helper(w1, w2):
            if len(w1) != len(w2):
                return False
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
                if cnt > 1:
                    return False
            return cnt == 1

        for word in wordList:
            if helper(word, beginWord):
                hm[word].add(beginWord)
                hm[beginWord].add(word)
        for i, w1 in enumerate(wordList):
            for j in range(i+1, len(wordList)):
                if helper(w1, wordList[j]):
                    hm[w1].add(wordList[j])
                    hm[wordList[j]].add(w1)
        
        dq = collections.deque()
        dq.append(beginWord)
        seen = collections.defaultdict(str)
        seen[beginWord] = None
        while len(dq) > 0:
            cur = dq.popleft()
            for nw in hm[cur]:
                if nw not in seen:
                    seen[nw] = cur
                    dq.append(nw)
                if nw == endWord:
                    break
        ans = collections.deque()
        if endWord not in seen:
            return []
        while endWord != beginWord:
            ans.appendleft(endWord)
            endWord = seen[endWord]
        ans.appendleft(endWord)
        return list(ans)