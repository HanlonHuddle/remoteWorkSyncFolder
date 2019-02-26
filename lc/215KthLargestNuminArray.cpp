// use priority_queue, remember, pq is max heap
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        if (nums.empty() || k==0)
            return -1;
        std::priority_queue<int> q;
        for (auto& num : nums)
        {
            q.push(num);
        }
        for (auto i=1; i<k; ++i)
        {
            q.pop();
        }
            
        return q.top();
    }
};