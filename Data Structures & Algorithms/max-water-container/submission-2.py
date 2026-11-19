class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        max_total = 0
        while (a < b):
            total = round(min(heights[a],heights[b]) * (b - a))
            if (total > max_total):
                max_total = total
            if (heights[a] > heights[b]):
                b -= 1
            else:
                a += 1

        return max_total