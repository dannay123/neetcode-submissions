class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        l, r = 0, 0
        res = 0
        last = {}

        while r < len(s):
            
            if s[r] in last and last[s[r]] >= l:
                l = last[s[r]] + 1
 
            last[s[r]] = r
            res = max(res, r - l + 1)
            r += 1


        return res
                