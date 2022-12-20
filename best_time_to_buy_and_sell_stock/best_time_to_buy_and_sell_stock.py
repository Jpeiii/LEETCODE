class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        maxProfits = 0
        n = len(prices)
        while sell < n:
            if prices[buy] < prices[sell]:
                currentProfit = prices[sell] - prices[buy]
                maxProfits = max(currentProfit, maxProfits)
            else:
                buy = sell
            sell += 1
        return maxProfits
