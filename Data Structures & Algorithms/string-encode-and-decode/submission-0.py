class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []
        for s in strs:
            pieces.append(str(len(s)) + "#" + s)
        return "".join(pieces)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            n = int (s[i:j])
            start = j + 1
            res.append(s[start:start + n])
            i = start + n
        return res            
