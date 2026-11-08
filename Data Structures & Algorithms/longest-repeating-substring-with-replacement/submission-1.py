class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        alpb = [0] * 26

        l, r = 0, 0
        freq = 0

        best = 0

        while r < len(s):


            alpb[ord(s[r]) - ord('A')] += 1
            freq = max (freq, alpb[ord(s[r]) - ord('A')])
            
            while ((r - l + 1) - freq) > k:

                alpb[ord(s[l]) - ord('A')] -= 1
                l += 1

            best = r - l + 1
            r += 1

        return best