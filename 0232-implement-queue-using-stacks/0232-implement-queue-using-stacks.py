class MyQueue(object):

    def __init__(self):
        self.popStack = []
        self.pushStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.pushStack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.popStack)>0:
            return self.popStack.pop()
        else:
            while len(self.pushStack)>0:
                elem = self.pushStack.pop()
                self.popStack.append(elem)
            return self.popStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.popStack)>0:
            return self.popStack[-1]
        while len(self.pushStack)>0:
            elem = self.pushStack.pop()
            self.popStack.append(elem)
        return self.popStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.popStack)+len(self.pushStack)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()