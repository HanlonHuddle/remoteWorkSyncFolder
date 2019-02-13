/*
 * @lc app=leetcode id=937 lang=java
 *
 * [937] Reorder Log Files
 *
 * https://leetcode.com/problems/reorder-log-files/description/
 *
 * algorithms
 * Easy (57.56%)
 * Total Accepted:    7.7K
 * Total Submissions: 13.3K
 * Testcase Example:  '["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]'
 *
 * You have an array of logs.  Each log is a space delimited string of words.
 * 
 * For each log, the first word in each log is an alphanumeric identifier.
 * Then, either:
 * 
 * 
 * Each word after the identifier will consist only of lowercase letters,
 * or;
 * Each word after the identifier will consist only of digits.
 * 
 * 
 * We will call these two varieties of logs letter-logs and digit-logs.  It is
 * guaranteed that each log has at least one word after its identifier.
 * 
 * Reorder the logs so that all of the letter-logs come before any digit-log.
 * The letter-logs are ordered lexicographically ignoring identifier, with the
 * identifier used in case of ties.  The digit-logs should be put in their
 * original order.
 * 
 * Return the final order of the logs.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
 * Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4
 * 7"]
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 0 <= logs.length <= 100
 * 3 <= logs[i].length <= 100
 * logs[i] is guaranteed to have an identifier, and a word after the
 * identifier.
 * 
 * 
 */
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        ArrayList<String> wdls = new ArrayList<String>();
        ArrayList<String> dils = new ArrayList<String>();
        for (String log : logs) {
            int si = log.indexOf(' ');
            if ('0' <= log.charAt(si+1) && log.charAt(si+1) <= '9')
                dils.add(log);
            else
                wdls.add(log);
        }
        Collections.sort(wdls, (a, b) -> { return a.substring(a.indexOf(' ')).compareTo(b.substring(b.indexOf(' '))); });
        wdls.addAll(dils);
        return wdls.toArray(new String[0]);
    }
}
