// dp

class Solution {
public:
    bool wordInDict(string s, vector<string>& wordDict)
    {
        for (auto& w : wordDict)
            if (s == w)
                return true;
        return false;
    }
    
    bool wordBreak(string s, vector<string>& wordDict) {
        int mem[s.length()+1]{};
        mem[0] = true;
        for (auto i=1; i<=s.length(); ++i)
        {
            for (auto j=1; j<=s.length()-i+1; ++j)
            {
                if (mem[i-1] && wordInDict(s.substr(i-1, j), wordDict))
                {
                    mem[i+j-1] = true;
                }
            }
        }
        
        return mem[s.length()];
    }
    
    
};