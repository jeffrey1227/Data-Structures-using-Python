class Stack():
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[-1]

    def push(self, value):
        self.array.append(value)
        return

    def pop(self):
        if len(self.array) == 0:
            return None
        returnValue = self.array.pop()
        return returnValue

    def printStack(self):
        print(self.array)
        return


stack = Stack()
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
stack.peek()
stack.push(4)
stack.printStack()
print(stack.pop())
stack.printStack()

