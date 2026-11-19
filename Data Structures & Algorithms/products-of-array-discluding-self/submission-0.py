class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)
        output = [None] * len(nums)

        for i in range(len(nums)):
            if (i == 0):
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1):
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i + 1]

        for i in range(len(nums)):
            if (i == 0):
                output[i] = suffix[i + 1]
            elif (i == len(nums) - 1):
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * suffix[i + 1]
        print(prefix)
        print(suffix)
        return output