class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l = 0;
        int r = 0;
        int size1 = word1.size();
        int size2 = word2.size();

        string res = "";
        int i = 0;
        while(l < size1 && r < size2)
        {
            if(i % 2 == 0)
                res += word1[l++];
            else
                res += word2[r++];
            i++;
        }

        while(l < size1)
            res += word1[l++];
        
        while(r < size2)
            res += word2[r++];
        
        return res;
    }
};