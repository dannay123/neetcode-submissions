class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)

    def binary_search(self, l: int, h: int, nums: List[int], target: int) -> int:
        if l > h:
            return -1
        m = l + (h-l)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binary_search(m + 1, h, nums, target)
        return self.binary_search(l, m - 1, nums, target)