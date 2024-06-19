class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Sets the comparison value to val if the minstack is empty
        if not self.minstack:
            comparison = val
        else:
            # Sets the comparison value to val if val is less than the current minimum value
            if val < self.minstack[-1]:
                comparison = val
            # Sets the comparison value to the current minimum if it is still less than val
            else:
                comparison = self.minstack[-1]
        # This appends the minimum between the comparison value and the current val to the minstack
        # This will give us the minimum value at the top of the minstack
        self.minstack.append(min(val, comparison))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()