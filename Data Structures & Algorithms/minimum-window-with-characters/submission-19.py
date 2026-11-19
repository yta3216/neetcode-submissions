class Solution:
    def minWindow(self, s: str, t: str) -> str:
        goal = Counter(t)
        have = 0
        output = float('inf')

        min_l = float('inf')
        min_r = float('inf')

        window = Counter()

        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if (window[s[r]] == goal[s[r]]):
                have += 1
            # check whether goal is a subset of the current string
            while (have == len(goal)):
                if (r - l <= output):
                    output = r - l
                    min_l = l
                    min_r = r + 1

    
                window[s[l]] -= 1
                if (window[s[l]] < goal[s[l]]):
                    have -= 1
                l += 1


        if (output == float('inf')): return ""
        return s[min_l:min_r]
            
