// Dummy solution with DFS:
// the tree looks like
//             1               2   3 .. 9
//       /            \       / \
//     10     11.........19   ...........
// /     \   /  \
// 100~109  110~119
// /\
// ......................................

class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ans;
        int cur = 1;
        for (cur=1; cur<10; ++cur)
            helper(n, cur, ans); 
        return ans;
    }
    void helper(int n, int cur, vector<int>& ans)
    {
        if (ans.size() == n)
            return;
        if (cur > n)
            return;
        else
            ans.push_back(cur);
        for (int i=0; i<=9; ++i)
            helper(n, cur*10+i, ans);
    }
};