class Solution {
public:
    void reverseString(vector<char>& s) {
        vector<char> rev(s.size());
        for (int i = 0; i<s.size(); i++){
            rev[s.size()-1-i] = s[i];
        }
        s = rev;
        // return rev;
    }
};