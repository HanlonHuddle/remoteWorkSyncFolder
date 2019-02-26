// THINKING IN A WRONG WAY !!!!!
// Simply use inorder traversa

// /**
//  * Definition for a binary tree node.
//  * struct TreeNode {
//  *     int val;
//  *     TreeNode *left;
//  *     TreeNode *right;
//  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//  * };
//  */
// class Solution {

// public:
//     unordered_map<TreeNode*, int> maxmem;
//     unordered_map<TreeNode*, int> minmem;
    
//     int findMax(TreeNode *node)
//     {
//         if (maxmem.find(node) == maxmem.end())
//             return maxmem[node];
        
//         if (node->left == NULL && node->right == NULL)
//         {
//             maxmem[node] = node->val;
//             return maxmem[node];
//         }
//         else if (node->left != NULL && node->right == NULL)
//         {
                        
//             maxmem[node] = max(findMax(node->left), node->val);
//             return maxmem[node];
//         }
//         else if (node->left == NULL && node->right != NULL)
//         {
//             maxmem[node] = max(findMax(node->right), node->val);
//             return maxmem[node];
//         }
//         else
//         {
//             int lrmax = max(findMax(node->left), findMax(node->right));
//             maxmem[node] = max(lrmax, node->val);
//             return maxmem[node];
//         }
//     }
    
//     int findMin(TreeNode *node)
//     {
//         if (minmem.find(node) == minmem.end())
//             return minmem[node];
        
//         if (node->left == NULL && node->right == NULL)
//         {
//             minmem[node] = node->val;
//             return minmem[node];
//         }
//         else if (node->left != NULL && node->right == NULL)
//         {
                        
//             minmem[node] = min(findMin(node->left), node->val);
//             return minmem[node];
//         }
//         else if (node->left == NULL && node->right != NULL)
//         {
//             minmem[node] = min(findMin(node->right), node->val);
//             return minmem[node];
//         }
//         else
//         {
//             int lrmin = min(findMin(node->left), findMin(node->right));
//             minmem[node] = min(lrmin, node->val);
//             return minmem[node];
//         }
//     }
    
//     bool isValidBST(TreeNode* root) {
//         if (root == NULL)
//             return true;
//         if (root->left == NULL && root->right == NULL)
//             return true;
//         else if (root->left != NULL && root->right != NULL)
//         {
//             if (findMin(root->left) > root->val || findMax(root->right) < root->val)
//                 return false;
//             if (!isValidBST(root->left) || !isValidBST(root->right))
//                 return false;
//             return true;
//         }
//         else if (root->left != NULL)
//         {
//             if (findMin(root->left) > root->val)
//                 return false;
//             if (!isValidBST(root->left))
//                 return false;
//             return true;
//         }
//         else
//         {
//             if (findMax(root->right) < root->val)
//                 return false;
//             if (!isValidBST(root-right))
//                 return false;
//             return true;
//         }
            
//         return true;
//     }
// };


// Good solution:

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
    bool isValidBST(TreeNode* root) {
        if (root == NULL)
            return true;
        stack<TreeNode*> st;
        TreeNode* cur = root;
        int last = 0;
        bool first = true;
        while (!st.empty() || cur!=NULL)
        {
            while (cur!=NULL)
            {
                st.push(cur);
                cur = cur->left;
            }
            if (cur == NULL)
            {
                if (first)
                {
                    last = st.top()->val;
                    first = false;
                }
                else
                {
                    if (st.top()->val <= last)
                        return false;
                    last = st.top()->val;
                }
                cur = st.top()->right;
                st.pop();
            }
        }
        
        return true;
    }
};

// another is to use threaded binary tree, move cur node to the rightmost of its left sub tree
//                                         if no left tree, add cur node cur = cur->nright