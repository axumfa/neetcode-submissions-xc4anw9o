class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> path;
        party(0, path, res, s);

        return res;
    }

    bool isPalindrome(string s)
    {
        int left = 0, right = s.size() - 1;

        while(left <= right)
        {
            if(s[left] != s[right])
                return false;
            left++;
            right--;
        }

        return true;
    }
    

    void party(int start, vector<string>& path, vector<vector<string>>& res, string& origin)
    {
        if(start == origin.size())
        {
            res.push_back(path);
        }

        for(int end = start; end < origin.size(); end++)
        {
            string subStr = origin.substr(start, end - start + 1);

            if(isPalindrome(subStr))
            {
                path.push_back(subStr);
                party(end + 1, path, res, origin);
                path.pop_back();
            }
        }
    }
};
