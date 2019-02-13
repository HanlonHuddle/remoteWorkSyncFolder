#
# @lc app=leetcode id=800 lang=python3
#
# [800] Similar RGB Color
#
# https://leetcode.com/problems/similar-rgb-color/description/
#
# algorithms
# Easy (58.42%)
# Total Accepted:    7K
# Total Submissions: 11.9K
# Testcase Example:  '"#09f166"'
#
# In the following, every capital letter represents some hexadecimal digit from
# 0 to f.
# 
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
# For example, "#15c" is shorthand for the color "#1155cc".
# 
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB -
# UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
# 
# Given the color "#ABCDEF", return a 7 character color that is most similar to
# #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"
# 
# 
# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:  
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64
# -9 -0 = -73.
# This is the highest among any shorthand color.
# 
# 
# Note:
# 
# 
# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0
# to f
# Any answer which has the same (highest) similarity as the best answer will be
# accepted.
# All inputs and outputs should use lowercase letters, and the output is 7
# characters.
# 
# 
#
class Solution:
    def similarRGB(self, color: 'str') -> 'str':
        ans = "#"
        for i in range(3):
            mdif = 18 * 18
            

            ori = (ord(color[1 + 2*i]) - ord('a')) * 16 + (ord(color[2 + 2*i]) - ord('a')) 
            ll = (ord(color[1 + 2*i]) - ord('a')) * 17
            rr = (ord(color[2 + 2*i]) - ord('a')) * 17
            if ll - ori > ori - rr:
                ans += color[2 + 2*i] + color[2 + 2*i]
            else:
                ans += color[1 + 2*i] + color[1 + 2*i]
        return ans
