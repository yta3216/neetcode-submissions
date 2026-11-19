class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while (l < r):
            nl = numbers[l]
            nr = numbers[r]

            res = nr + nl
            if (res > target):
                r -= 1
            elif (res == target):
                return [l + 1, r + 1]
            else:
                l += 1