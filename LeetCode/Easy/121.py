class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = prices[0]

        for price in prices[1:]:
            if buy < price:
                result = max(result, price-buy)
            else:
                buy = price

        return result
        
