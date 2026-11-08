class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        alpb = [0] * 26

        l, r = 0, 0
        freq = 0

        best = 0

        while r < len(s):

            indexr = ord(s[r]) - ord('A')
            indexl = ord(s[l]) - ord('A')

            alpb[indexr] += 1
            freq = max (freq, alpb[indexr])
            
            while ((r - l + 1) - freq) > k:

                alpb[indexl] -= 1
                l += 1

            best = r - l + 1
            r += 1

        return best