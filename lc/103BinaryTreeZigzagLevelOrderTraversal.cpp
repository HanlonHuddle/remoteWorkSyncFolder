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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        stack<TreeNode*> s1, s2, *sp, *sp2;
        vector<vector<int>> ans{};
        if (!root)
            return ans;
        vector<int> curv{};
        sp = &s1;
        sp2 = &s2;
        s1.push(root);
        int tms = 1;
        
        while(!sp->empty())
        {
            curv.push_back(sp->top()->val);
            
            if (tms % 2 == 0)
            {
                if (sp->top()->right)
                    sp2->push(sp->top()->right);
                if (sp->top()->left)
                sp2->push(sp->top()->left);
            }
            else
            {
                if (sp->top()->left)
                    sp2->push(sp->top()->left);
                if (sp->top()->right)
                sp2->push(sp->top()->right);
            }
            sp->pop();
            if(sp->empty())
            {
                tms++;
                ans.push_back(curv);
                curv.clear();
                swap(sp, sp2);    
            }
        }
            
        return ans; 
    }
};