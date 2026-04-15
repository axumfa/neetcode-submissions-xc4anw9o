class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1 
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]

        left = 1 
        for i in range(len(nums)-1,-1,-1):
            res[i] *= left
            left *= nums[i]
        return res