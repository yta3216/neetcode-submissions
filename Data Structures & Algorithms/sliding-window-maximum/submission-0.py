class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = collections.deque()
        res = []

        l = 0
        for r in range(len(nums)):
            while stack and stack[-1] < nums[r]:
                stack.pop()

            stack.append(nums[r])

            if (r - l + 1 > k):
                if stack[0] == nums[l]:
                    stack.popleft()
                l += 1
            
            if (r - l + 1 == k):
                res.append(stack[0])

        return res

