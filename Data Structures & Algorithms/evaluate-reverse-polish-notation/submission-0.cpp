class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (int i = 0; i < tokens.size(); i++){
            if (tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/") {
                int right = stk.top();
                stk.pop();
                int left = stk.top();
                stk.pop();
                int res;
                if (tokens[i] == "+") res = left + right;
                else if (tokens[i] == "-") res = left - right;
                else if (tokens[i] == "*") res = left * right;
                else res = left / right;
                stk.push(res);
            } else {
                stk.push(stoi(tokens[i]));
            }
        }
        return stk.top();
    }
};