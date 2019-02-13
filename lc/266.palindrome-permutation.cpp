/*
 * @lc app=leetcode id=266 lang=cpp
 *
 * [266] Palindrome Permutation
 *
 * https://leetcode.com/problems/palindrome-permutation/description/
 *
 * algorithms
 * Easy (59.12%)
 * Total Accepted:    58.5K
 * Total Submissions: 98.7K
 * Testcase Example:  '"code"'
 *
 * Given a string, determine if a permutation of the string could form a
 * palindrome.
 * 
 * Example 1:
 * 
 * 
 * Input: "code"
 * Output: false
 * 
 * Example 2:
 * 
 * 
 * Input: "aab"
 * Output: true
 * 
 * Example 3:
 * 
 * 
 * Input: "carerac"
 * Output: true
 * 
 */
class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> cnt;
        for (auto& c : s) 
            cnt[c] += 1;
        
        int odd = 0;

        for (auto& p : cnt)
            if (p.second % 2 != 0)
                odd += 1;
        
        return odd < 2;
    }
};
