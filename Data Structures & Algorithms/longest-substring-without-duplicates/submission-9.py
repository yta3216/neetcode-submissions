class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = {}
        out = 0
        while right < len(s):
            char = s[right]
            if not window.get(char) or window.get(char) == 0:
                window[char] = 1
                right += 1
            else:
                while (window.get(char) > 0):
                    window[s[left]] -= 1
                    left += 1
            out = max(out, right - left)
        return out