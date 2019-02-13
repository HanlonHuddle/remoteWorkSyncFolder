#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (42.73%)
# Total Accepted:    25.3K
# Total Submissions: 59.2K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
# 
# Example 1:
# 
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
# 
# 
# 
# Example 2:
# 
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# 
# 
# 
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
# 
#
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        maxl = 0
        ls = [""]
        s = set(words)
        for word in words:
            cpword = word
            ol = len(word)
            while len(word) > 0 and word in s:
                word = word[0:-1]
            if len(word) == 0:
                if not ls or maxl < ol:
                    maxl = ol
                    ls = []
                    ls.append(cpword)
                elif maxl == ol:
                    ls.append(cpword)
        return sorted(ls)[0]
