// Should think about using iterative soluation not recersive

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int n{};
    int ans{};
    int cap{};
    void inorder(TreeNode* root)
    {
        if (n >= cap)
            return;
        if (!root)
            return;
        if (root->left)
            inorder(root->left);
        // cout << root->val << endl;
        n++;
        if (n == cap)
        {
            ans = root->val;
            return;
        }
        if (root->right)
            inorder(root->right);
    }
    int kthSmallest(TreeNode* root, int k) {
        cap = k;
        inorder(root);
        
        return ans;
    }
};