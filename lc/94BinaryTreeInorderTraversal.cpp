/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// 1) Create an empty stack S.
// 2) Initialize current node as root
// 3) Push the current node to S and set current = current->left until current is NULL
// 4) If current is NULL and stack is not empty then 
//      a) Pop the top item from stack.
//      b) Print the popped item, set current = popped_item->right 
//      c) Go to step 3.
// 5) If current is NULL and stack is empty then we are done.

// good Solution and explain
// https://leetcode.com/problems/binary-tree-inorder-traversal/solution/


// http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if (!root)
            return result;
        
        stack<TreeNode*> st;
        TreeNode* cur = root;
        while(!st.empty() || cur!=NULL)
        {
            while(cur!=NULL)
            {
                st.push(cur);
                cur = cur->left;
            }
            if (cur == NULL && !st.empty())
            {
                result.push_back(st.top()->val);
                cur = st.top()->right;
                st.pop();
            }
        }
        return result;
    }
};