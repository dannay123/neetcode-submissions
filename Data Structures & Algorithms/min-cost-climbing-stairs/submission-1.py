class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * n
        
        def dp(i):
            if i == n:
                return 0
            if cache[i] != -1:
                return cache[i]
            one = dp(i + 1)
            two = dp(i + 2) if i + 2 <= n else float('inf')
            cache[i] = cost[i] + min(one, two)
            return cache[i]
        return min(dp(0), dp(1))