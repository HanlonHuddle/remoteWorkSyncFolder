#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (51.97%)
# Total Accepted:    73.3K
# Total Submissions: 141K
# Testcase Example:  '"USA"'
#
# 
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# 
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter,
# like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# Input: "USA"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# Note:
# The input will be a non-empty word consisting of uppercase and lowercase
# latin letters.
# 
#
class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return None
        if 'a' <= word[0] <= 'z':
            for c in word:
                if c < 'a' or c > 'z':
                    return False
            return True
        elif 'A' <= word[0] <= 'Z':
            r1, r2 = True, True
            for i in range(1, len(word)):
                if 'a' > word[i] or 'z' < word[i]:
                    r1 = False
                if 'A' > word[i] or 'Z' < word[i]:
                    r2 = False
            return r1 or r2
        return False
