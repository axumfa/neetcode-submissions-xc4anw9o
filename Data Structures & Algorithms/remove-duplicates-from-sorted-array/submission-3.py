class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        cur_pos = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[cur_pos] = nums[i]
                cur_pos += 1
        
        return cur_pos