/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * Using stack
 */
 class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1;
        stack<int> s2;
        while (l1)
        {
            s1.push(l1->val);
            l1 = l1-> next;
        }
        while (l2)
        {
            s2.push(l2->val);
            l2 = l2->next;
        }
        
        int tmp = 0;
        ListNode* result = NULL;
        
        while (!s1.empty() || !s2.empty())
        {
            int a, b;
            if (s1.empty())
                a = 0;    
            else
            {
                a = s1.top();
                s1.pop();
            }
            
            if (s2.empty())
                b = 0;    
            else
            {
                b = s2.top();
                s2.pop();
            }
            
            int cur = (a + b + tmp) % 10;
            tmp = (a + b + tmp) / 10;
            
            ListNode* ln = result;
            result = new ListNode(cur);
            result->next = ln;
        }
        if (tmp != 0)
        {
            ListNode* ln = result;
            result = new ListNode(tmp);
            result->next = ln;
        }
        
        return result;
    }
};