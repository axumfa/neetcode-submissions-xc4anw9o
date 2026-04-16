class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        int size = digits.size();
        

        for(int i = size - 1; i >= 0; i--)
        {
            int total = digits[i] + carry;
            digits[i] = total % 10;
            carry = total / 10;
        }   
        if(carry)
        {
            vector<int> res(size + 1);
            res[0] = carry;
            for(int i = 0; i < size; i++)
                res[i + 1] = digits[i];
            return res;
        }

        return digits;
    }
};
