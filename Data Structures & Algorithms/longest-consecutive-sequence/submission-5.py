class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0
        for num in lookup:
            if (num-1) not in lookup:
                cur = num
                count = 0
                while cur in lookup:
                    count += 1
                    cur += 1
                longest = max(longest, count)
        return longest         
