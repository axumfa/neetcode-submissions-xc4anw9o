class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        
        int total = 0;
        backtrack(0, 0, total, nums);

        return total;

    }

    void backtrack(int place, int curXor, int& total, vector<int>& nums)
    {
        if(place == nums.size())
        {
            total += curXor;
            return;
        }
        
        backtrack(place + 1, curXor ^ nums[place], total, nums);

        backtrack(place + 1, curXor, total, nums);

    }
};