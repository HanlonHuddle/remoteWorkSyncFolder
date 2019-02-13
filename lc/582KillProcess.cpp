// use tree simulation
// since pid is unique, we can use map+vector instead

class myTreeNode
{
public:
    int pid;
    vector<myTreeNode*> childs;
    myTreeNode(int processid):
    pid(processid)
    {
    }
};

class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {
        vector<int> result;
        unordered_map<int, myTreeNode*> treemap;
        
        for (int i=0; i<pid.size(); ++i)
            treemap[pid[i]] = new myTreeNode(pid[i]);
        
        for (int i=0; i<ppid.size(); ++i)
            if (ppid[i] != 0)
                treemap[ppid[i]]->childs.push_back(treemap[pid[i]]);
        
        stack<int> st;
        st.push(kill);
        while (!st.empty())
        {
            result.push_back(st.top());
            int curpid = st.top();
            st.pop();
            for (myTreeNode* tn : treemap[curpid]->childs)
                st.push(tn->pid);
        }
        return result;
    }
};