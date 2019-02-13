/*
 * @lc app=leetcode id=872 lang=java
 *
 * [872] Leaf-Similar Trees
 *
 * https://leetcode.com/problems/leaf-similar-trees/description/
 *
 * algorithms
 * Easy (60.99%)
 * Total Accepted:    28.9K
 * Total Submissions: 47.1K
 * Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
 *
 * Consider all the leaves of a binary tree.  From left to right order, the
 * values of those leaves form a leaf value sequence.
 * 
 * 
 * 
 * For example, in the given tree above, the leaf value sequence is (6, 7, 4,
 * 9, 8).
 * 
 * Two binary trees are considered leaf-similar if their leaf value sequence is
 * the same.
 * 
 * Return true if and only if the two given trees with head nodes root1 and
 * root2 are leaf-similar.
 * 
 * 
 * 
 * Note:
 * 
 * 
 * Both of the given trees will have between 1 and 100 nodes.
 * 
 * 
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public void leafIter(TreeNode root, ArrayList<Integer> tmp) {
        if (root == null)
            return;
        if (root.left != null)
            leafIter(root.left, tmp);
        if (root.left == null && root.right == null)
            tmp.add(root.val);
        if (root.right != null)
            leafIter(root.right, tmp);
    }
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> res1 = new ArrayList<Integer>();
        ArrayList<Integer> res2 = new ArrayList<Integer>();
        leafIter(root1, res1);
        leafIter(root2, res2);

        if (res1.size() != res2.size())
            return false;
        
        for (int i=0; i<res1.size(); i++) {
            if (res1.get(i) != res2.get(i))
                return false;
        }

        return true;
    }
}
