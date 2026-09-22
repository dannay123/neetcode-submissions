class Solution:
    def climbStairs(self, n: int) -> int:
        cache = n * [-1] 
        def helper(i):
            if i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            one = helper(i + 1)
            two = helper(i + 2) if (i + 2) <= n else 0
            cache[i] = one + two
            return cache[i]
        return helper(0)