/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//  using recersive calls to do so, remember to set two if here.

class Solution {
public:
    void helper(vector<int>& preorder, vector<int>& inorder, int a, int b, int i, int j, TreeNode*& root)
    {
        if (a > b)
            return;
        root = new TreeNode(preorder[a]);
        if (a == b)
            return;
        int q{};
        for (q=i; q<=j; ++q)
            if (inorder[q] == root->val)
                break;
        int p = a + q - i;
        helper(preorder, inorder, a+1, p, i, q-1, root->left);
        helper(preorder, inorder, p+1, b, q+1, j, root->right);
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        TreeNode* root{};
        int a{}, b{preorder.size()-1}, i{}, j{inorder.size()-1};
        helper(preorder, inorder, a, b, i, j, root);
        return root;
    }
};