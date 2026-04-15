class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxPrice = 0
        minPrice = prices[0]

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxPrice = max(maxPrice,price - minPrice)

        return maxPrice