class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = defaultdict(int)
        l = 0
        max_length = 0

        for r in range(len(s)):
            window[s[r]] += 1
            if (r - l + 1 - max(window.values()) > k):
                window[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length


