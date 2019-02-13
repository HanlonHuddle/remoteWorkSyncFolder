#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#
# https://leetcode.com/problems/valid-word-abbreviation/description/
#
# algorithms
# Easy (28.74%)
# Total Accepted:    20.2K
# Total Submissions: 70.3K
# Testcase Example:  '"internationalization"\n"i12iz4n"'
#
# 
# Given a non-empty string s and an abbreviation abbr, return whether the
# string matches with the given abbreviation.
# 
# 
# A string such as "word" contains only the following valid abbreviations:
# 
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 
# Notice that only the above abbreviations are valid abbreviations of the
# string "word". Any other string is not a valid abbreviation of "word".
# 
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase
# letters and digits.
# 
# 
# Example 1:
# 
# Given s = "internationalization", abbr = "i12iz4n":
# 
# Return true.
# 
# 
# 
# Example 2:
# 
# Given s = "apple", abbr = "a2e":
# 
# Return false.
# 
# 
#
class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if 'a' <= abbr[j] <= 'z':
                if abbr[j] != word[i]: return False
                else: 
                    i += 1
                    j += 1
            else:
                ts = []
                while j < len(abbr) and '0' <= abbr[j] <= '9':
                    ts.append(abbr[j])
                    j += 1
                num = int(''.join(ts))
                if num == 0 or num != 0 and ts[0] == '0':
                    return False
                i += num
        if i != len(word) or j != len(abbr):
            return False
        return True
