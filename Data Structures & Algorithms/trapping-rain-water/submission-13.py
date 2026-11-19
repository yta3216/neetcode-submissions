class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        max_l = 0
        for i in range(len(height)):
            if height[i] > max_l:
                max_l = height[i]
            prefix[i] = max_l
            
        max_r = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > max_r:
                max_r = height[i]
            suffix[i] = max_r

        total = []
        for i in range(len(height)):
            res = min(prefix[i], suffix[i]) - height[i]
            total.append(max(0, res))
        return sum(total)

