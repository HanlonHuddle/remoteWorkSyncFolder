// There is on inplace soluation by traversal from both ends of arrays, and put them inorder at the end of nums1
// please refer to the one line code which is cool
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> ans;
        unsigned i{}, j{};
        while (ans.size() < m + n)
        {
            if (i<m && j<n)
            {
                if (nums1[i] < nums2[j])
                {
                    ans.push_back(nums1[i]);
                    ++i;
                }
                else
                {
                    ans.push_back(nums2[j]);
                    ++j;
                }
            }
            else if(i==m)
            {
                ans.push_back(nums2[j]);
                ++j;
            }
            else
            {
                ans.push_back(nums1[i]);
                ++i;
            }
        }
        swap(nums1, ans);
    }
};