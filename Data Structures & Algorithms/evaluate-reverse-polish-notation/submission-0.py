class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operator = ["+", "-", "/", "*"]

        stack = []
        for i in tokens:
            if i in operator:
                right = stack.pop()
                left = stack.pop()
                if (i == "+"):
                    result = int(left) + int(right)
                
                elif (i == "-"):
                    result = int(left) - int(right)

                elif (i == "*"):
                    result = int(left) * int(right)

                else:
                    result = int(left) / int(right)
                print(result)
                stack.append(result)
            else:
                stack.append(i)
        return int(stack[0])