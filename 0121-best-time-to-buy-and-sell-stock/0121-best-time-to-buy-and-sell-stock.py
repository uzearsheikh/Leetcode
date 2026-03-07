class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = prices[0]
        profit = 0
        for i in prices:
            # agar price minprice se choti hai to usko minprice krlo
            if i<min_price:  
                min_price = i
                # profit = sell price - minprice
            profit = max(profit , i - min_price)

        return profit
        