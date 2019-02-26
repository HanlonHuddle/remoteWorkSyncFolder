class Solution {
public:
    int trailingZeroes(int n) {
        int ans = 0;
        double t = n;
        while (t >= 5)
        {
            ans += int(t/5);
            t/=5;
        }
        
        return ans;
    }
};

// Remember!!! 5 25 5^3 ...