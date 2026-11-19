
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        needed = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                if stack.pop() != needed[c]:
                    return False

        return len(stack) == 0