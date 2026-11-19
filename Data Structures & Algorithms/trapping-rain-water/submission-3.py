class Solution:
    def trap(self, height: List[int]) -> int:


        total_water = []
        for i in range(0, len(height) - 1):
            
            # check left
            max_l = 0
            for l in range(0, i):
                if (height[l] > height[max_l]):
                    max_l = l
                    
            # check right
            max_r = len(height) - 1
            for r in range(i, len(height) - 1):
                if (height[r] > height[max_r]):
                    max_r = r
            water = min(height[max_l], height[max_r]) - height[i]
            total_water.append(max(0, water))
        return sum(total_water)

        return 0