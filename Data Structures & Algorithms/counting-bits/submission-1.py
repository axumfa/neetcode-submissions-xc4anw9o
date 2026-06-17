class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            c = 0
            while i > 0:
                c += i & 1
                i >>= 1
            
            res.append(c)
        
        return res