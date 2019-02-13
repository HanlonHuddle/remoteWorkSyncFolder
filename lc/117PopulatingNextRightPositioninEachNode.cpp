/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
using namespace std;

class Solution {
public:
    void connect(TreeLinkNode *root) {
        queue<TreeLinkNode *> qt;
        queue<TreeLinkNode *> nl;
        if (root != NULL)
            qt.push(root);
        while(qt.size() != 0)
        {
            TreeLinkNode *ptln = qt.front();
            qt.pop();
            
            if (ptln->left != NULL)
                nl.push(ptln->left);
            if (ptln->right != NULL)
                nl.push(ptln->right);
            
            if (qt.empty())
            {
                ptln->next = NULL;
                swap(qt, nl);  
            }
            else
            {
                ptln->next = qt.front();
            }
        }
    }
};