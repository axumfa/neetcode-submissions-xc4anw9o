class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;
        int size = s.size();
        int l = 0;
        int r = 0;

        for(int i = 0; i < size; i++)
        {
            l = i, r = i;
            while(l >= 0 && r < size && s[l--] == s[r++])
                res++;
            
            l = i, r = i + 1;
            while(l >= 0 && r < size && s[l--] == s[r++])
                res++;
        }

        return res;
    
    }

};
