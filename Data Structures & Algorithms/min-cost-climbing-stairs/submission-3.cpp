class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int size = cost.size();
        vector<int> arr(size);
        arr[0] = cost[0];
        arr[1] = cost[1];
        for(int i = 2; i < size; i++)
        {
            arr[i] = min(arr[i - 2], arr[i - 1]) + cost[i]; 
            // [1, 2, 3]
        }

        return min(arr[size - 2],arr[size - 1]);
        
    }
};
