// good idea, from [] add num to each element in vector. repeat
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> f;
        result.push_back(f);
        for (auto& n : nums)
        {
            auto len = result.size();
            for (auto i=0; i<len; ++i)
            {
                vector<int>* pv = new vector<int>(result[i]);
                pv->push_back(n);
                result.push_back(*pv);
            }
        }
        return result;
    }
};

// more geneural one, use backtracking. like DFS:
// 1             10
//            /      \
// 2       10           10
//       /    \       /   \
// 3    10     10     10    10
//     / \    / \    / \   /  \
//    1   1  1   1  2   2  3   []
//    2   2  3      3       
//    3

