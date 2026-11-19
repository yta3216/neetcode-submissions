# instinct:
# all you have to look for is when the list starts decreasing
# have l, r pointer
# check if num[r] >= num[l]
# if it is, the list is sorted, just return nums[l]
# if num[r] < num[l], move l up half the array

# revised, no way to tell if answer will be on the left or right
# will indiscriminately favor right side
# soln: introduce middle, compare num[r] and num[l] against

class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        while (l < r):
            mid = l + (r - l) // 2
            if (nums[mid] > nums[r]):
                l = mid + 1
            elif (nums[mid] < nums[r]):
                r = mid
        return nums[l]
