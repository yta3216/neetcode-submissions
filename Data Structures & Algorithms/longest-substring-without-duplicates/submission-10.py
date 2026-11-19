# Optimal Solution:
# - instead of using for loop to move the left pointer,
# - jump directly to correct position by storing index in 
# - the hashmap

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0

        res = 0

        for r in range(len(s)):
            if s[r] in window:
                left = max(window[s[r]] + 1, left)
            window[s[r]] = r
            res = max(res, r - left + 1)
        return res