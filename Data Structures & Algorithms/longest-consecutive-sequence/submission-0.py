class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in range(len(nums)):
            
            if nums[i] - 1 not in num_set:
                cnt = 1
                current_num = nums[i]

                while current_num + 1 in num_set:
                    cnt += 1
                    current_num += 1
                
                longest = max(cnt,longest)
        return longest