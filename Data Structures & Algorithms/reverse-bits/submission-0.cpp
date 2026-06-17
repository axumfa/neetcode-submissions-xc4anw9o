class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        uint32_t a = n;

        for(int i = 0; i < 32; i++)
        {
            res = res << 1 ;
            res |= (a & 1);
            a >>= 1;
        }
        return res;
    }
};
