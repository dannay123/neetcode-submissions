import heapq
class KthLargest:
    k = 0
    nums = []

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        kth = []
        for i in self.nums:
            heapq.heappush(kth, i)
            if len(kth) > self.k:
                heapq.heappop(kth)
        return kth[0]
