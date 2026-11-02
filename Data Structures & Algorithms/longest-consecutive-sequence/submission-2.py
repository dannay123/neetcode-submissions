from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0
        for i in nums:
            count = 0
            if (i-1) not in lookup:
                while i in lookup:
                    count += 1
                    i += 1
            longest = max(longest, count)
        return longest         
