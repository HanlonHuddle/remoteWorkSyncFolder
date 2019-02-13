/*
 * @lc app=leetcode id=949 lang=cpp
 *
 * [949] Largest Time for Given Digits
 *
 * https://leetcode.com/problems/largest-time-for-given-digits/description/
 *
 * algorithms
 * Easy (31.46%)
 * Total Accepted:    5.2K
 * Total Submissions: 16K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an array of 4 digits, return the largest 24 hour time that can be
 * made.
 * 
 * The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
 * 00:00, a time is larger if more time has elapsed since midnight.
 * 
 * Return the answer as a string of length 5.  If no valid time can be made,
 * return an empty string.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,3,4]
 * Output: "23:41"
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [5,5,5,5]
 * Output: ""
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * A.length == 4
 * 0 <= A[i] <= 9
 * 
 * 
 * 
 */
class Solution {
public:
    string largestTimeFromDigits(vector<int>& A) {
        unordered_map<int, int> mp;
        for (auto& a : A) {
            if (a < 0 || a > 9)
                return "";
            mp[a] += 1;
        }
        for (short h=23; h>=0; --h)
            for (short m=59; m>=0; --m) {
                string hs = to_string(h);
                string ms = to_string(m);
                short h1=0, h2=0, m1=0, m2=0;
                if (hs.size() == 1) {
                    h1 = 0;
                    h2 = stoi(hs);
                }
                else {
                    h1 = (hs[0] - '0');
                    h2 = (hs[1] - '0');
                }
                if (ms.size() == 1) {
                    m1 = 0;
                    m2 = stoi(ms);
                }
                else {
                    m1 = (ms[0] - '0');
                    m2 = (ms[1] - '0');
                }
                mp[h1] -= 1;
                mp[h2] -= 1;
                mp[m1] -= 1;
                mp[m2] -= 1;
                if (mp[h1] == 0 && mp[h2] == 0 && mp[m1] == 0 && mp[m2] == 0)
                    return to_string(h1) + to_string(h2) + ":" + to_string(m1) + to_string(m2);
                mp[h1] += 1;
                mp[h2] += 1;
                mp[m1] += 1;
                mp[m2] += 1;
            }
        return "";
    }
};
