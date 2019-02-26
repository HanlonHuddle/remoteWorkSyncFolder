// [0,1,0,2,1,0,1,3,2,1,2,1]

// for O(1) and stack solution see the solution. it is good!
// https://leetcode.com/problems/trapping-rain-water/solution/

// AC O(n^2)
class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        for (auto i=0; i<height.size(); ++i)
        {
            int lmax = 0;
            int rmax = 0;
            for (auto l=0; l<i; ++l)
                lmax = max(lmax, height[l]);
            for (auto r=i+1; r<height.size(); ++r)
                rmax = max(rmax, height[r]);
            int bar = min(rmax, lmax);
            if (bar > height[i])
                ans += bar - height[i];
        }
        return ans;
    }
};


// DP, O(n) space: O(n)
class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        vector<int> maxl(height.size());
        vector<int> maxr(height.size());
        
        for (auto i=0; i<height.size(); ++i)
        {
            if (i==0)
            {
                maxl[i] = height[i];
                maxr[height.size()-1-i] = height[height.size()-1-i];
            }
            else 
            {
                maxl[i] = max(maxl[i-1], height[i]);
                maxr[height.size()-1-i] = max(maxr[height.size()-i], height[height.size()-i]);
            }
        }
        
        for (auto i=0; i<height.size(); ++i)
        {
            int bar = min(maxl[i], maxr[i]);
            if (bar > height[i])
                ans += bar - height[i];
        }
        return ans;
    }
};