#
# @lc app=leetcode id=555 lang=python3
#
# [555] Split Concatenated Strings
#
# https://leetcode.com/problems/split-concatenated-strings/description/
#
# algorithms
# Medium (39.41%)
# Total Accepted:    3.5K
# Total Submissions: 8.8K
# Testcase Example:  '["abc","xyz"]'
#
# Given a list of strings, you could concatenate these strings together into a
# loop, where for each string you could choose to reverse it or not. Among all
# the possible loops, you need to find the lexicographically biggest string
# after cutting the loop, which will make the looped string into a regular
# one.
# 
# Specifically, to find the lexicographically biggest string, you need to
# experience two phases: 
# 
# Concatenate all the strings into a loop, where you can reverse some strings
# or not and connect them in the same order as given.
# Cut and make one breakpoint in any place of the loop, which will make the
# looped string into a regular one starting from the character at the
# cutpoint. 
# 
# 
# 
# And your job is to find the lexicographically biggest one among all the
# possible regular strings.
# 
# 
# Example:
# 
# Input: "abc", "xyz"
# Output: "zyxcba"
# Explanation: You can get the looped string "-abcxyz-", "-abczyx-",
# "-cbaxyz-", "-cbazyx-", where '-' represents the looped status. The answer
# string came from the fourth looped one, where you could cut from the middle
# character 'a' and get "zyxcba".
# 
# 
# 
# Note:
# 
# The input strings will only contain lowercase letters.
# The total length of all the strings will not over 1,000.
# 
# 
#
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        ans = None
        for i in range(len(strs)):
            strs[i] = strs[i] if strs[i] >= strs[i][::-1] else strs[i][::-1]
        cand = None
        candps = []
        for i, word in enumerate(strs):
            for j, c in enumerate(word):
                if cand == None or cand == c:
                    cand = c
                    candps.append((i, j))
                elif cand < c:
                    cand = c
                    candps = [(i, j)]

        ans = None

        def helper(cord):
            nonlocal strs
            ans = ''.join(strs[cord[0]][cord[1]::])

            i = cord[0] + 1
            if i >= len(strs):
                i = 0
            while i != cord[0]:
                ans += strs[i]
                i += 1
                if i >= len(strs):
                    i = 0
                
            ans += ''.join(strs[cord[0]][:cord[1]:])
            return ans

        for cand in candps:
            strs[cand[0]] = strs[cand[0]][::-1]
            tans1 = helper((cand[0], len(strs[cand[0]])-1-cand[1]))
            strs[cand[0]] = strs[cand[0]][::-1]
            tans2 = helper(cand)

            tans = tans1 if tans1 > tans2 else tans2
            ans = tans if (ans == None or tans > ans) else ans

        return ans


