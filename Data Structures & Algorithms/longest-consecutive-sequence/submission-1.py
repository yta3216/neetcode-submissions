class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = set(nums)
        max = 0
        for i in l:
            if (i - 1 not in l):
                count = 0
                current = i
                while (current in l):
                    count += 1
                    current += 1
                if (count > max):
                    max = count
        return max