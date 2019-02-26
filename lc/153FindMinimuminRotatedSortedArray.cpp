class Solution {
public:
    int helper(vector<int>& nums, int a, int b)
    {
        if (a == b)
            return nums[a];
        if (a == b-1)
            return min(nums[a], nums[b]);
        int mid = (a+b)/2;
        if ((nums[mid] < nums[a] && nums[mid] < nums[b]) || (nums[mid] > nums[a] && nums[mid] < nums[b]))
            return helper(nums, a, mid);
        else
            return helper(nums, mid, b);
    }
    
    int findMin(vector<int>& nums) {
        return helper(nums, 0, nums.size()-1);
    }
    
};