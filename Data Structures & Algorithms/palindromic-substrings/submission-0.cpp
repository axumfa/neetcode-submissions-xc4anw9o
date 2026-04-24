class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;

        int size = s.size();
        for(int i = 0; i < size; i++)
        {
            // odd length
            int l = i, r = i;
            while(l >= 0 && r < size && s[l--] == s[r++])
                res++;
            
            // even length
            l = i, r = i + 1;
            while(l >= 0 && r < size && s[l--] == s[r++])
                res++;

        }
        return res;
    }


};
