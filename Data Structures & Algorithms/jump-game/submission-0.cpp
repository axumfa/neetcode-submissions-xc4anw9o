class Solution {
public:
    bool canJump(vector<int>& nums) {
        int length = nums.size();
        int goal = length - 1;

        for(int i=length - 2; i >= 0; i--)
        {
            if (i + nums[i] >= goal)
                goal = i;
        }

        return (goal == 0) ? true : false; 
    }
};
