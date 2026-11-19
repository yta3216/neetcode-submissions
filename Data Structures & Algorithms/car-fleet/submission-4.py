class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = collections.deque()

        times = []
        for i in range(len(position)):
            times.append((target - position[i]) / speed[i])
        times = [x for _, x in sorted(zip(position, times), reverse=True)]

        for i in range(len(times)):
            if stack and times[i] <= stack[-1]:
                continue
            else:
                stack.append(times[i])
        return len(stack)