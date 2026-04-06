class Solution {
public:
    double myPow(double x, int n) {
        double res = 1;
        int cnt = abs(n);
        while(cnt){
            res *= x;
            cnt--;
        }
        if (n<0){
            return(1/res);
        }
        return res;
    }
};
