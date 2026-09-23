from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = defaultdict(list)    
        for str in strs:

            tb = [0] * 26

            for c in str:
                tb[ord(c) - ord('a')] += 1

            key = tuple(tb)

            hash[key].append(str)
        return list(hash.values())