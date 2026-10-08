class Solution {
public:
    int getSum(int a, int b) {
        int tmp = 0;

        while(b != 0)
        {
            tmp = (a & b) << 1;
            a = a ^ b;
            b = tmp;
        }   
        
        return a;
    }
};
