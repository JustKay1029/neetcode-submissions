class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # keep track of the lowest price so far (best day to buy)
            if price < min_price:
                min_price = price
            # profit if we sell today
            profit = price - min_price
            # update max profit
            if profit > max_profit:
                max_profit = profit

        return max_profit