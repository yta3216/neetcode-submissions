class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (i == '{' or i == '(' or i == '['):
                stack.append(i)
                continue
            if (len(stack) == 0):
                return False
            out = stack.pop()
            if (out == '{' and i == '}'):
                continue
            if (out == '[' and i == ']'):
                continue
            if (out == '(' and i == ')'):
                continue
            return False
        if (len(stack) == 0): return True
        else: return False
