class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1
        
        for p1 in range(0, len(numbers)):
            for p2 in range(p1, len(numbers)):
                if (p1 == p2):
                    continue
                if (numbers[p1] + numbers[p2] == target):
                    return [p1 + 1, p2 + 1]
            
        