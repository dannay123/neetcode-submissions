class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        curr = 0
        for i in range (1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            curr = max(curr, prices[i] - buy)
        return curr