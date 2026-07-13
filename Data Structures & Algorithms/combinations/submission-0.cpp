class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> p;
        vector<vector<int>> res;

        backtrack(1, n, k, p, res);

        return res;
    }

    void backtrack(int start, int n, int k, vector<int>& path, vector<vector<int>>& res)
    {
        if(path.size() == k)
        {
            res.push_back(path);
            return;
        }

        for(int i = start; i <= n; i++)
        {
            path.push_back(i);
            backtrack(i + 1, n, k, path, res);
            path.pop_back();
        }
    }
};