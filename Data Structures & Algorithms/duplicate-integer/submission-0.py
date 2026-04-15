class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic1 = {x: nums.count(x) for x in nums}
        for key in dic1:
            if dic1[key] > 1:
                return True
        return False