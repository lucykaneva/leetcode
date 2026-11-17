class MinStack:

    def __init__(self):
       self.storage = [] 
       self.min = []

    def push(self, value: int) -> None:
        self.storage.append(value)
        if len(self.min) == 0 or self.min[len(self.min)-1] >= value:
            self.min.append(value)

    def pop(self) -> None:
        if len(self.min)>0 and self.min[len(self.min)-1] == self.storage[len(self.storage)-1]:
            self.min.pop()
        self.storage.pop()


    def top(self) -> int:
        return self.storage[len(self.storage)-1]

    def getMin(self) -> int:
        return self.min[len(self.min)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()