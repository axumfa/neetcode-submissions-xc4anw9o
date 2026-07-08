class Solution {
public:
    int rob(vector<int>& nums) {
        
        int size = nums.size();
        
        if(size == 1)
            return nums[0];
        int prev2 = nums[0];
        int prev1 = max(nums[0], nums[1]);

        for(int i = 2; i < size; i++)
        {
            int cur = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }

        return prev1;
    }
};
