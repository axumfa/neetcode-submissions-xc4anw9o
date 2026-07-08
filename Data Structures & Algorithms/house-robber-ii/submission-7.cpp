class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        
        if(nums.size() < 2)
            return nums[0];
        
        int size = nums.size();
        return max(robber(nums, 0, size - 1), robber(nums, 1, size));
    }

    int robber(vector<int>& nums, int start, int end)
    {
        if(start + 1 == end)
            return nums[start];

        int prev2 = nums[start];
        int prev1 = max(prev2, nums[start + 1]);
        int cur = 0;
    
        for(int i = start + 2; i < end; i++)
        {
            cur = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;
    
    }

};