class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        need = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                if stack.pop() != need[c]:
                    return False
        return len(stack) == 0