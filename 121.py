class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        minn = prices[0]
        max_profit = 0
        for price in prices:
            if price < minn:
                minn = price
            current_profit = price - minn
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit

print(Solution().maxProfit(prices = [1, 10, 2, 25]))