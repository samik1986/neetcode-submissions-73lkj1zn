class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        for (int i = 0; i<32; i++){
            uint32_t bit = (n>>i) & 1;
            if (bit){
                res+=1;
            }
        }
        return res;
    }
};
