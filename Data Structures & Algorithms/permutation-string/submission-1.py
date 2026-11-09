from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        check = defaultdict(int)

        for i in s1:
            check[i] += 1

        l, r = 0, k

        while r < len(s2) + 1:

            has = defaultdict(int)

            for i in range(l, r):
                has[s2[i]] += 1
            
            if has == check:
                return True

            l, r = l + 1, r + 1

        return False


                
                
                
                
        
