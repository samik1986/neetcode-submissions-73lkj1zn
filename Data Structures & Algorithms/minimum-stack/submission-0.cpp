class MinStack {

private:
    stack<int> stk;
    // stack<int> minstk;

public:
    MinStack() {}
    
    void push(int val) {
        stk.push((val));
    }
    
    void pop() {
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        stack<int> tmp;
        int minVal = stk.top();
        while(stk.size()){
            minVal = min(minVal, stk.top());
            tmp.push(stk.top());
            stk.pop();
        }
        while(tmp.size()){
            stk.push(tmp.top());
            tmp.pop();
        }
        return minVal;
        
    }
};
