from collections import Counter, defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, j in Counter(nums).items():
            if len(heap) < k:
                heapq.heappush(heap, (j, i))
            else:
                heapq.heappushpop(heap, (j,i))
        return [v for f, v in heap]
            

