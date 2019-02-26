// priority queue
// how to overload for object pointer queue
// compare string alphabetical:
// https://stackoverflow.com/questions/15212820/do-and-on-c-strings-reflect-alphabetical-ordering

class Item
{
public:
    string name;
    int times;
    Item(string na, int ti):
    name(na), times(ti)
    {}
    
};

struct nodeCompairson
{
    bool operator() (const Item* lhs, const Item* rhs)
    {
        return lhs->times == rhs->times ? lhs->name.compare(rhs->name)>0 : lhs->times < rhs->times;
    }
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        vector<string> result;
        
        unordered_map<string, int> m;
        for (auto& word : words)
            if (m.find(word) != m.end())
                m[word]++;
            else
                m[word] = 1;
        
        priority_queue<Item*, vector<Item*>, nodeCompairson> pq;
        for (auto& pair : m)
            pq.push(new Item(pair.first, pair.second));
        
        while (k > 0)
        {
            result.push_back(pq.top()->name);
            pq.pop();
            --k;
        }
        
        return result;
    }
};