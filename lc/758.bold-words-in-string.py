#
# @lc app=leetcode id=758 lang=python3
#
# [758] Bold Words in String
#
# https://leetcode.com/problems/bold-words-in-string/description/
#
# algorithms
# Easy (40.73%)
# Total Accepted:    6.1K
# Total Submissions: 14.9K
# Testcase Example:  '["ab","bc"]\n"aabcd"'
#
# 
# Given a set of keywords words and a string S, make all appearances of all
# keywords in S bold.  Any letters between <b> and </b> tags become bold.
# 
# The returned string should use the least number of tags possible, and of
# course the tags should form a valid combination.
# 
# 
# For example, given that words = ["ab", "bc"] and  S = "aabcd", we should
# return "a<b>abc</b>d".  Note that returning "a<b>a<b>b</b>c</b>d" would use
# more tags, so it is incorrect.
# 
# 
# Note:
# words has length in range [0, 50].
# words[i] has length in range [1, 10].
# S has length in range [0, 500].
# All characters in words[i] and S are lowercase letters.
# 
#
class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        mk = [0]*len(S)
        for word in words:
            if word in S:
                for i in range(S.find(word), S.find(word)+len(word)):
                    mk[i] = 1

        ls = []
        for i, m in enumerate(mk):
            if i == 0:
                if m == 1:
                    ls.append("<b>" + S[i])
                else:
                    ls.append(S[i])
            else:
                if m == 1:
                    if mk[i-1] != 1:
                        ls.append("<b>" + S[i])
                    else:
                        ls.append(S[i])
                if m == 0:
                    if mk[i-1] == 1:
                        ls.append("</b>" + S[i])
                    else:
                        ls.append(S[i])
        if mk[-1] == 1:
            ls.append("</b>")
        return ''.join(ls)
                
