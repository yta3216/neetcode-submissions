class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights) - 1
        max_water = 0
        while (a < b):
            water = int(min(heights[b], heights[a]) * (b - a))
            if (water > max_water):
                max_water = water
            if (heights[a] <= heights [b]):
                a += 1
            else:
                b -= 1
        return max_water
