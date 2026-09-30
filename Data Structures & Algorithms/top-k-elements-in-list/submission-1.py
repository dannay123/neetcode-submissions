from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nandf = Counter(nums)
        bucket = [[] for _ in range (n + 1)]
        res = []
        for i, j in nandf.items():
            bucket[j].append(i)
        for i in range (n, 0, -1):
            if bucket[i]:
                res += bucket[i]
            if len(res) == k:
                break
        return res