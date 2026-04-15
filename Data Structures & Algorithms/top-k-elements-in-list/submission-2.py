class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            if nums[i] not in numbers:
                numbers[nums[i]] = 0
            numbers[nums[i]] += 1
        
        res = sorted(numbers.items(),key=lambda x: x[1],reverse=True)
        return [item[0] for item in res[:k]]       
