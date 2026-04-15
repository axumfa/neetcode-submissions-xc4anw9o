class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1
        minN = nums[0]
        
        while r >= l:
            if nums[l] < nums[r]:
                minN = min(minN, nums[l])
                break
            mid = l + (r - l) // 2
            minN = min(minN,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return minN