class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> res;

        dfs(0, nums, path, res);
        return res;
    }

    void dfs(int c, vector<int>&nums, vector<int> p, vector<vector<int>>& r)
    {
        if(c == nums.size())
        {
            r.push_back(p);
            return;
        }

        
        dfs(c + 1, nums, p, r);

        p.push_back(nums[c]);
        dfs(c + 1, nums, p, r);
        p.pop_back();
    }
};
