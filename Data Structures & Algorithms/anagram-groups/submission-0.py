from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = defaultdict(list)    
        for str in strs:

            tb = [0] * 26

            for i in range(len(str)):
                tb[ord(str[i]) - ord('a')] += 1

            key = tuple(tb)

            hash[key].append(str)
        return list(hash.values())