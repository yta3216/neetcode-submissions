class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = collections.deque()
        
        r = len(nums) - 1
        l = 0
        while (l <= r):
            if (abs(nums[l]) > abs(nums[r])):
                res.appendleft(nums[l] * nums[l])
                l += 1
            else:
                res.appendleft(nums[r] * nums[r])
                r -= 1
        return list(res)