class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1 , 2, 4, 4]
        prev1 = 0
        prev2 = 0

        for n in nums:
            cur = max(prev1, n + prev2)
            prev2 = prev1
            prev1 = cur


        return prev1