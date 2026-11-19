class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = [None] * len(height)
        right_max = [None] * len(height)
        total_water = []
        
        max_r = 0 # pointer of highest wall at right
        for i in range(0, len(height)):
            if (height[i] > max_r):
                max_r = height[i]
            left_max[i] = max_r

        max_l = 0 # pointer of highest wall at left
        for i in range(len(height) - 1, -1, -1):
            if (height[i] > max_l):
                max_l = height[i]
            right_max[i] = max_l

        for i in range(0, len(height)):
            water = min(left_max[i], right_max[i]) - height[i]
            total_water.append(max(0, water))
        return sum(total_water)
        