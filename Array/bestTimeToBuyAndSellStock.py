from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for price in prices[1:]:
            maxProfit = max(maxProfit, price-minPrice)
            minPrice = min(minPrice, price)
        return maxProfit




