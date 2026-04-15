class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = piles[0]
        for i in range(len(piles)):
            right = max(right,piles[i])

        res = right
        
        while left <= right:
            mid = left + (right - left ) // 2
            time = 0
            for i in range(len(piles)):
                if piles[i] % mid > 0:
                    time += piles[i] // mid + 1
                else:
                    time += piles[i] // mid
            if time <= h:
                res = min(mid,res) 
                right = mid - 1
            else:
                left = mid + 1
        return res
            