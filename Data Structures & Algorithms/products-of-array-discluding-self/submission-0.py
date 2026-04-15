class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []
        product = 1
        for i in range(len(nums)):
            left.append(product)
            product *= nums[i]
        
        right = [1] * len(nums)
        product = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = product
            product *= nums[i]
        
        Output = []
        for i in range(len(nums)):
            Output.append(left[i]*right[i])

        return Output