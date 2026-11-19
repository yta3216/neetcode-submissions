class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use bs to find cut first

        l = 0
        r = len(nums) - 1

        while (l < r):
            m = l + (r - l) // 2
            if (nums[l] > nums[m]):
                r = m
            elif (nums[m] > nums[r]):
                l = m + 1
            else:
                r = m
                
        pivot = l
        if (target <= nums[-1]):
            c_l = pivot
            c_r = len(nums) - 1
        else:
            c_l = 0
            c_r = pivot - 1

        # then perform bs on cut
        while (c_l <= c_r):
            m = c_l + (c_r - c_l) // 2
            if (nums[m] < target):
                c_l = m + 1
            elif (nums[m] > target):
                c_r = m - 1
            else:
                return m
        return -1