class newNode():
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
    return

class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    return

  def append(self, value):
    if self.head == None:
      self.head = newNode(value)
      self.tail = self.head
    else:
      self.tail.next = newNode(value)
      self.tail = self.tail.next
    self.length += 1
    return

  def prepend(self, value):
    if self.head == None:
      self.head = newNode(value)
      self.tail = self.head
    else:
      node = newNode(value)
      node.next = self.head
      self.head = node
    self.length += 1
    return

  def insert(self, index, value):
    # check params
    if index == 0:
      self.prepend(value)
    elif index >= self.length:
      self.append(value)
    else:
      current = self.head
      for i in range(index-1):
        current = current.next
      node = newNode(value)
      node.next = current.next
      current.next = node
      self.length += 1
    return

  def remove(self, index):
    if index == 0:
      node = self.head
      self.head = self.head.next
      del node
    elif index >= self.length:
      node = self.tail
      current = self.head
      for i in range(self.length-2):
        current = current.next
      self.tail = current
      self.tail.next = None
      del node
    else:
      current = self.head
      for i in range(index-1):
        current = current.next
      node = current.next
      current.next = node.next
      del node

    self.length -= 1
    return

  def reverse(self):
    cur1 = self.head
    cur2 = cur1.next
    while(cur2 != None):
      next = cur2.next
      cur2.next = cur1
      cur1 = cur2
      cur2 = next

    self.tail = self.head
    self.tail.next = None
    self.head = cur1

    return


  def printList(self):
    current = self.head
    for i in range(self.length):
      print(current.value, end = " ")
      if current.next != None:
        print("-->", end = " ")
        current = current.next
    print("")


class DoublyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    return

  def append(self, value):
    if self.head == None:
      self.head = newNode(value)
      self.tail = self.head
    else:
      node = newNode(value)
      self.tail.next = node
      node.prev = self.tail
      self.tail = self.tail.next
    self.length += 1
    return

  def prepend(self, value):
    if self.head == None:
      self.head = newNode(value)
      self.tail = self.head
    else:
      node = newNode(value)
      node.next = self.head
      self.head.prev = node
      self.head = node
    self.length += 1
    return

  def insert(self, index, value):
    # check params
    if index == 0:
      self.prepend(value)
    elif index >= self.length:
      self.append(value)
    else:
      current = self.head
      for i in range(index-1):
        current = current.next
      node = newNode(value)
      node.next = current.next
      current.next.prev = node
      current.next = node
      node.prev = current
      self.length += 1
    return

  def remove(self, index):
    if index == 0:
      node = self.head
      self.head = self.head.next
      self.head.prev = None
      del node
    elif index >= self.length:
      node = self.tail
      self.tail = self.tail.prev
      self.tail.next = None
      del node
    else:
      if index < self.length / 2:
        current = self.head
        for i in range(index-1):
          current = current.next
      else:
        current = self.tail
        for i in range(self.length - index):
          current = current.prev
      node = current.next
      current.next = node.next
      node.next.prev = current
      del node

    self.length -= 1
    return


  def printList(self):
    print("Frontwards")
    current = self.head
    for i in range(self.length):
      print(current.value, end = " ")
      if current.next != None:
        print("-->", end = " ")
        current = current.next
    print("")
    print("Backwards")
    current = self.tail
    for i in range(self.length):
      print(current.value, end = " ")
      if current.prev != None:
        print("-->", end = " ")
        current = current.prev
    print("\n\n")


# doubly = DoublyLinkedList()
# doubly.append(2)
# doubly.append(3)
# doubly.append(5)
# doubly.printList()
# doubly.prepend(1)
# doubly.insert(3, 4)
# doubly.insert(5, 6)
# doubly.printList()
# doubly.remove(3)
# doubly.printList()


singly = LinkedList()
singly.append(2)
singly.append(3)
singly.append(5)
singly.prepend(1)
singly.insert(3, 4)
singly.insert(5, 6)
singly.remove(3)
singly.printList()
singly.reverse()
singly.printList()
    
