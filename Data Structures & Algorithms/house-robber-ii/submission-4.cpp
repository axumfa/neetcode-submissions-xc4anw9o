class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() < 2)
        {
            return nums[0];
        }
        int size = nums.size();
        return max(helper(0, size - 1, nums), helper(1, size, nums));
    }
    int helper(int start, int end, vector<int>& nums)
    {
        int prev1 = 0;
        int prev2 = 0;
        
        for(int i = start; i < end; i++)
        {
            int cur = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
};
