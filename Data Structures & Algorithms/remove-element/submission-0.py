class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0

        for n in nums:
            if n != val:
                nums[cnt] = n
                cnt += 1
        
        return cnt
            