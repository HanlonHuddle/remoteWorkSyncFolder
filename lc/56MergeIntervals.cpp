// Some cases shoud consider
// sort, if b.start > a.end pushback b
// else if b.end > a.end merge pop push_back

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */

struct myComp
{
public:
    bool operator() (const Interval &a, const Interval &b)
    {
        return a.start == b.start ? a.end < b.end : a.start < b.start;
    }
};

class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        if (intervals.empty())
            return intervals;
        sort(intervals.begin(), intervals.end(), myComp());
        
        vector<Interval> result;
        result.push_back(intervals[0]);
        for (auto &i : intervals)
        {
            if (result.back().end >= i.start)
            {
                if (result.back().end < i.end)
                {
                    Interval itv(result.back().start, i.end);
                    result.pop_back();
                    result.push_back(itv);    
                }
            }
            else
                result.push_back(i);
        }
        return result;
    }
};