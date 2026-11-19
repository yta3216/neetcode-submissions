class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for p1 in range(0, len(nums) - 2):
            if (p1 > 0 and nums[p1] == nums[p1 - 1]):
                continue
            p2 = p1 + 1
            p3 = len(nums) - 1
            while (p2 < p3):
                val = nums[p1] + nums[p2] + nums[p3]
                if val == 0:
                    output.append([nums[p1] , nums[p2] , nums[p3]])
                    p2 += 1
                    p3 -= 1

                    # skip dupes for l
                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1
                    
                    # skip duples for r
                    while p2 < p3 and p3 < len(nums) - 1 and nums[p3] == nums[p3 + 1]:
                        p3 -=1
                
                elif val < 0:
                    p2 +=1
                else:
                    p3 -=1

        return output

            