class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k%=nums.size();
        if (k==0)
            return;
        vector<int> tem(nums);
        for (int i=0; i<nums.size(); ++i)
        {
            nums[k] = tem[i];
            k++;
            k = k >= nums.size() ? 0 : k;
        }
        return;
    }
};