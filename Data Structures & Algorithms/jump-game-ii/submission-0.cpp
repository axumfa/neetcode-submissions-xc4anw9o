class Solution {
public:
    int jump(vector<int>& nums) {
        int right = 0;
        int left = 0;
        int maxReach = 0;
        int length = nums.size() - 1;
        int res = 0;


        while(right < length)
        {
            for(int i = left; i <= right; i++)
            {
                maxReach = max(maxReach, nums[i] + i);
            }
            left += 1;
            right = maxReach;
            res++;
        }

        return res;
    }
};
