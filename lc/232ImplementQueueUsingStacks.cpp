// basic stack useage, using two stacks for getting things
// try ask push, pop which is used more

class MyQueue {
public:
    /** Initialize your data structure here. */
    // sa is queue order, sb is reverse order as a helper
    std::stack<int> sa, sb;
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        sa.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (sa.empty())
            // if every thing good never come here
            return -1;
        else
        {
            while (!sa.empty())
            {
                sb.push(sa.top());
                sa.pop();
            }
            int result = sb.top();
            sb.pop();
            while (!sb.empty())
            {
                sa.push(sb.top());
                sb.pop();
            }
            return result;
        }
    }
    
    /** Get the front element. */
    int peek() {
        if (sa.empty())
            // if every thing good never come here
            return -1;
        else
        {
            while (!sa.empty())
            {
                sb.push(sa.top());
                sa.pop();
            }
            int result = sb.top();
            while (!sb.empty())
            {
                sa.push(sb.top());
                sb.pop();
            }
            return result;
        }
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return sa.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * bool param_4 = obj.empty();
 */