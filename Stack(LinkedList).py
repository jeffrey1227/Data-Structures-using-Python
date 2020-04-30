class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top == None:
            return None
        return self.top.value

    def push(self, value):
        newNode = Node(value)
        if self.top == None:
            self.top = newNode
            self.bottom = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return

    def pop(self):
        if self.top == None:
            return None
        returnValue = self.top.value
        unwanted = self.top
        self.top = self.top.next
        if self.top == None: # Only one item
            self.bottom = None
        self.length -= 1
        del unwanted
        return returnValue

    def printStack(self):
        current = self.top
        print("====Stack=====")
        while current != None:
            print(current.value)
            if current.next != None:
                print("|")
            current = current.next
        print("==============")
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

