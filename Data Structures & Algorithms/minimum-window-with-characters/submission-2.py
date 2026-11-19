class Solution:
    def minWindow(self, s: str, t: str) -> str:
        goal = Counter(t)
        output = s
        result = float('inf')


        l = 0
        for r in range(len(s) + 1):
            # check whether goal is a subset of the current string
            while (Counter(s[l:r]) >= goal):
                output = min(output, s[l:r], key=len)
                result = min(len(output), result)
                l += 1
        if (result == float('inf')): return ""
        return output
            
