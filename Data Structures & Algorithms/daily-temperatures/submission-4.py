class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ind = collections.deque()
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            curr = temperatures[i]

            while ind and temperatures[ind[-1]] < curr:
                res[ind[-1]] = i - ind[-1]
                ind.pop()
                
            ind.append(i)

        return res
