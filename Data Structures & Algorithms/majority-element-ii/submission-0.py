class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums) // 3

        elements = {}

        for n in nums:
            elements[n] = elements.get(n, 0) + 1
        
        res = []
        for n in elements:
            if elements[n] > length:
                res.append(n)
        
        return res