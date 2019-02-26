#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (22.75%)
# Total Accepted:    229.3K
# Total Submissions: 1M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# Note:
# 
# 
# Return 0 if there is no such transformation sequence.
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
# Output: 5
# 
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
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
# Output: 0
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
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        def path(w1, w2):
            if len(w1) != len(w2):
                return False
            diffcnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diffcnt += 1
                if diffcnt > 1:
                    return False
            return diffcnt == 1
        
        hm = collections.defaultdict(list)

        wordList.append(beginWord)

        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if path(wordList[i], wordList[j]):
                    hm[wordList[i]].append(wordList[j])
                    hm[wordList[j]].append(wordList[i])
        
        if endWord not in hm:
            return 0
        
        anshm = collections.defaultdict(int)
        anshm[beginWord] = 1

        dq = collections.deque()
        dq.append(beginWord)
        anshm[beginWord] = 1
        while len(dq) > 0:
            cur = dq.popleft()
            for node in hm[cur]:
                if node not in anshm:
                    anshm[node] = anshm[cur] + 1
                    dq.append(node)
        
        return anshm[endWord] if endWord in anshm else 0
        
        
