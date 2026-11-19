class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        stack = collections.deque()

        for i in s:
            if i not in brackets:
                stack.append(i)
            else:
                if not stack or brackets[i] != stack.pop():
                    return False
        
        if stack: return False
        else: return True
