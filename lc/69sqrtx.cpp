class Solution {
public:
    int mySqrt(int x) {
        return int(sqrt(x));
    }
};

class Solution {
public:
    int mySqrt(int x) {
        if (x <= 0)
            return x;
        long long ans = x;
        while (ans * ans > x)
            ans /= 2;
        while (ans * ans < x)
            ans += 1;
        if (ans * ans > x)
            ans -= 1;
        return ans;
    }
};

// wrong answer, also see ans = ans - ans/2 + x/ans/2
class Solution {
public:
    int mySqrt(int x) {
        long ans = x;
        while (ans * ans > x)
        {
            ans = ans/2 + x/ans/2;
        }
        return ans;
    }
};

// works simple and stupid
class Solution {
public:
    int mySqrt(int x) {
        long r = x;
        while (r*r > x)
            r = (r + x/r) / 2;
        return r;
    }
};