class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif self.minstack and self.minstack[-1] >= val:
            self.minstack.append(val)


    def pop(self) -> None:
        out = self.stack.pop()
        if self.minstack and out == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1]
        else: return None 

    def getMin(self) -> int:
        if self.minstack: return self.minstack[-1]
        else: return None
