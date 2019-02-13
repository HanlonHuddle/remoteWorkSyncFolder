/*
 * @lc app=leetcode id=500 lang=java
 *
 * [500] Keyboard Row
 *
 * https://leetcode.com/problems/keyboard-row/description/
 *
 * algorithms
 * Easy (61.04%)
 * Total Accepted:    78.8K
 * Total Submissions: 128.7K
 * Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
 *
 * Given a List of words, return the words that can be typed using letters of
 * alphabet on only one row's of American keyboard like the image
 * below.
 * 
 * 
 * 
 * 
 * 
 * 
 * Example:
 * 
 * 
 * Input: ["Hello", "Alaska", "Dad", "Peace"]
 * Output: ["Alaska", "Dad"]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * You may use one character in the keyboard more than once.
 * You may assume the input string will only contain letters of alphabet.
 * 
 * 
 */
class Solution {
    public String[] findWords(String[] words) {
        HashSet<Character> hs1 = new HashSet<>(Arrays.asList('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'));
        HashSet<Character> hs2 = new HashSet<>(Arrays.asList('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'));
        HashSet<Character> hs3 = new HashSet<>(Arrays.asList('z', 'x', 'c', 'v', 'b', 'n', 'm'));

        ArrayList<String> ans = new ArrayList<>();

        int idx = 0;

        for (String wordor : words) {
            boolean tmp = true;
            String word = wordor.toLowerCase();
            if (hs1.contains(word.charAt(0))) {
                for (int i=0; i<word.length(); i++) 
                    if (!hs1.contains(word.charAt(i)))
                    {
                        tmp = false;
                        break;

                    }
            }
            else if (hs2.contains(word.charAt(0))) {
                for (int i=0; i<word.length(); i++) 
                    if (!hs2.contains(word.charAt(i))) {
                        tmp = false;
                        break;

                    }
            }
            else 
                for (int i=0; i<word.length(); i++) 
                    if (!hs3.contains(word.charAt(i)))
                        tmp = false;
            
            if (tmp)
                ans.add(wordor);
        }
        return ans.toArray(new String[0]);
    }
}
