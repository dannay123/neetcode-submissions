from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ccount = {}
        ccount1 = {}
        for c in s:
            ccount[c] = ccount.get(c,0) + 1
        for c in t:
            ccount1[c] = ccount1.get(c,0) + 1
        return ccount == ccount1