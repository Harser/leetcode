class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minn = prices[0]
        maxx = prices[0]
        ans =  0
        for i in range(1, len(prices)):
            if prices[i - 1] > prices[i]:
                ans += (maxx - minn)
                maxx = prices[i]
                minn = prices[i]
            if prices[i] < minn:
                ans = maxx - minn
                minn = prices[i]
            if prices[i] > maxx:
                maxx = prices[i]
        ans += maxx - minn
        return ans