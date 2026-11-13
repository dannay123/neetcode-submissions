class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can(k):

            hours = 0

            for i in piles:

                hours += (i + k - 1) // k 

                if hours > h:
                    return False

            return True 
        lo , hi = 1, max(piles)

        while lo < hi:

            mid = lo + (hi - lo) // 2

            if can(mid):
                hi = mid

            else:
                lo = mid + 1
        
        return lo

    
        