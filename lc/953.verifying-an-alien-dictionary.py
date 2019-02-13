#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
#
# algorithms
# Easy (57.24%)
# Total Accepted:    9K
# Total Submissions: 15.9K
# Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
#
# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.
# 
# 
# 
# Example 2:
# 
# 
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] >
# words[1], hence the sequence is unsorted.
# 
# 
# 
# Example 3:
# 
# 
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is
# shorter (in size.) According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character which is less
# than any other character (More info).
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.
# 
# 
# 
# 
# 
#
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) < 2:
            return True

        hm = {}
        for i in range(len(order)):
            hm[order[i]] = i

        def decending(w1, w2):
            nonlocal hm
            i = 0
            while i < len(w1) and i < len(w2) and w1[i] == w2[i]:
                i += 1
            if i < len(w1) and i < len(w2) and hm[w1[i]] > hm[w2[i]]:
                    return True
            if w2 in w1 and w1.find(w2) == 0:
                return True
            return False
        
        for i in range(len(words) - 1):
            if decending(words[i], words[i+1]):
                return False
        
        return True
