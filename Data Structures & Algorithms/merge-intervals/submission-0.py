class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        res = []

        for i in intervals:
            if not res:
                res.append(i)
                continue

            recent = res[-1]
            if (recent[1] < i[0]):
                res.append(i)
                continue

            recent[1] = max(recent[1], i[1])

        return res

