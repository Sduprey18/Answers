class MinStack:

    def __init__(self):
        self.arr = []
        self.minStack = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        _min = min(self.minStack[-1],val) if self.minStack else val
        self.minStack.append(_min)
        

    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()