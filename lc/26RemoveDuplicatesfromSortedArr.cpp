class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0;
        int j=1;
        int len = nums.size();
        int ans = 0;
        if (nums.size() <= 1)
        {
            return len-ans;
        }
        
        while (j < nums.size())
        {
            if (nums[i] == nums[j])
            {
                nums.erase(nums.begin()+j);
                ans++;
            }
                
            else
            {
                i++;
                j++;
            }
        }
        
        return len-ans;
    }
};