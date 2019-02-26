class Solution {
public:
    double myPow(double x, int n) {
        long nn = n;
        if (nn == 0)
            return 1;
        if (nn < 0)
        {
            x = 1 / x;
            nn = -nn;
        }
            
        if (nn&1)
            return x * myPow(x*x, nn/2);
        else
            return myPow(x*x, nn/2);
    }
};