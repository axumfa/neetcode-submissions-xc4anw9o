class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1 = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in dic1:
                return [dic1[complement],i]
            dic1[num] = i