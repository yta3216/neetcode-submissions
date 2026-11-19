class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:      
        hm = {}
        hm = defaultdict(int)
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if (diff in hm):
                return [hm[diff], i]
            else:
                hm[nums[i]] = i