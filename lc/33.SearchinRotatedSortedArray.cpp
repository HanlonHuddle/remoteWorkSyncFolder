class Solution {
public:
    int helper(vector<int>& nums, int a, int b, const int& target)
    {
        if (a == b)
            return nums[a]==target ? a:-1;
        if (a == b-1)
        {
            if (nums[a] == target)
                return a;
            if (nums[b] == target)
                return b;
            return -1;
        }
        int L = nums[a];
        int R = nums[b];
        int m = (a+b)/2;
        int M = nums[m];
        
        if (L > R)
        {
            if (target >= L)
            {
                if ((M>L && M>target) || (M<L))
                    return helper(nums, a, m, target);
                else
                    return helper(nums, m, b, target);
            }
            else
            {
                if ((M>L) || (M<R && M<target))
                    return helper(nums, m, b, target);
                else
                    return helper(nums, a, m, target);
            }
        }
        else
        {
            if (M<target)
                return helper(nums, m, b, target);
            else
                return helper(nums, a, m ,target);
        }
    }
    
    int search(vector<int>& nums, int target) {
        if (nums.size()==0)
            return -1;
        return helper(nums, 0, nums.size()-1, target);
    }
    
};