class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.bottom == None:
            return None
        else:
            return self.bottom.value

    def enqueue(self, value):
        newNode = Node(value)
        if self.bottom == None:
            self.bottom = newNode
            self.top = newNode
            return
        self.top.next = newNode
        self.top = self.top.next
        self.length += 1
        return

    def dequeue(self):
        if self.bottom == None:
            return None
        else:
            returnValue = self.bottom.value
            if self.bottom == self.top:
                self.top = None
            self.bottom = self.bottom.next
            self.length -= 1
        return returnValue

    def printQueue(self):
        current = self.bottom
        while(current != None):
            print(current.value, end=' ')
            current = current.next
        print("")
        return

queue = Queue()
queue.dequeue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.peek())
print(queue.dequeue())
queue.printQueue()