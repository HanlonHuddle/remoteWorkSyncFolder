/*
 * @lc app=leetcode id=821 lang=cpp
 *
 * [821] Shortest Distance to a Character
 *
 * https://leetcode.com/problems/shortest-distance-to-a-character/description/
 *
 * algorithms
 * Easy (61.63%)
 * Total Accepted:    26.7K
 * Total Submissions: 43.1K
 * Testcase Example:  '"loveleetcode"\n"e"'
 *
 * Given a string S and a character C, return an array of integers representing
 * the shortest distance from the character C in the string.
 * 
 * Example 1:
 * 
 * 
 * Input: S = "loveleetcode", C = 'e'
 * Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * S string length is in [1, 10000].
 * C is a single character, and guaranteed to be in string S.
 * All letters in S and C are lowercase.
 * 
 * 
 */
class Solution {
public:
    vector<int> shortestToChar(string S, char C) {
        int i = 0;
        vector<int> poi;
        for (int x=0; x<S.size(); ++x) 
            if (S[x] == C)
                poi.push_back(x);
        vector<int> ans;
        for (int x=0; x<S.size(); ++x) {
            while (i < poi.size() - 1 && poi[i + 1] <= x) {
                i += 1;
            }
            if (i < poi.size() - 1)
                ans.push_back(min(abs(poi[i+1] - x), abs(x - poi[i])));
            else
                ans.push_back(abs(x - poi[i]));
        }
        return ans;
    }
};
