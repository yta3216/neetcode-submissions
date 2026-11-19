class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        inc = True
        dec = True
        for i in range(len(nums) - 1):
            n = nums[i + 1]
            prev = nums[i]
            if (n > prev):
                dec = False
            elif (n < prev):
                inc = False
            if not inc and not dec:
                return False

        return True