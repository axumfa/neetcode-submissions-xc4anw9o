class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        MAX = nums[0]

        for i in range(1, len(nums)):
            curMax = max(curMax + nums[i], nums[i])
            MAX = max(MAX, curMax)
        
        return MAX