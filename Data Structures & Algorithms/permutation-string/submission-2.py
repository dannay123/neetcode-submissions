from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)

        if k > len(s2):
            return False
        
        check = Counter(s1)
        has = Counter(s2[i] for i in range(k))

        if has == check:
            return True

        for r in range (k, len(s2)):
            
            if has == check:
                return True

            l = r - k
            
            has[s2[l]] -= 1
            
            if has[s2[l]] == 0:
                del has[s2[l]]
            
            has[s2[r]] += 1
            
            if has == check:
                return True
                
        return False


                
                
                
                
        
