class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0
        for i in lookup:
            if (i-1) not in lookup:
                count = 0
                while i in lookup:
                    count += 1
                    i += 1
                longest = max(longest, count)
        return longest         
