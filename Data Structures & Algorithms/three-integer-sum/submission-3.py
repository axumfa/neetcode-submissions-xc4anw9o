class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = len(nums) - 1
            k = i + 1
            while k < j:
                if nums[i] + nums[k] + nums[j] == 0:
                    res.append([nums[i],nums[k],nums[j]])
                    k += 1
                    j -= 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                    while k < j and nums[j] == nums[j+1]:
                        j -= 1

                elif nums[i] + nums[k] + nums[j] > 0:
                    j -= 1
                elif nums[i] + nums[k] + nums[j] < 0:
                    k += 1
        return res