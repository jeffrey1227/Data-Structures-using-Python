class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return
        
        current = self.root
        while(True):
            if value > current.value:
                if current.right != None:
                    current = current.right
                else:
                    current.right = newNode
                    return
            else:
                if current.left != None:
                    current = current.left
                else:
                    current.left = newNode
                    return
                

    def lookup(self, value):
        if self.root == None:
            return False
        
        current = self.root

        while(True):
            if value == current.value:
                return current
            elif value > current.value:
                if current.right != None:
                    current = current.right
                else:
                    return False
            elif value < current.value:
                if current.left != None:
                    current = current.left
                else:
                    return False

    def traverseInOrder(self, node):
        current = node
        if current.left != None:
            self.traverseInOrder(current.left)
        print(current.value)
        if current.right != None:
            self.traverseInOrder(current.right)

    def traversePreOrder(self, node):
        current = node
        print(current.value)
        if current.left != None:
            self.traversePreOrder(current.left)
        if current.right != None:
            self.traversePreOrder(current.right)
        return

    def traversePostOrder(self, node):
        current = node
        if current.left != None:
            self.traversePostOrder(current.left)

        if current.right != None:
            self.traversePostOrder(current.right)
        print(current.value)

    def BFS(self):
        queue = [self.root]
        while(queue):
            current = queue.pop(0)
            print(current.value)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return


    def remove(self, value):
        if self.root == None:
            return None
        current = self.root
        parent = None
        # find the node we want to remove
        while(True):
            if value > current.value:
                if current.right == None:
                    return None
                parent = current
                current = current.right
            elif value < current.value:
                if current.left == None:
                    return None
                parent = current
                current = current.left

            elif value == current.value:
                # find the minimal value in the right subtree
                # Situation 1: node has no right child
                if current.right == None:
                    if current.left == None:
                        if parent == None:
                            self.root = None
                        elif parent.value > current.value:
                            parent.left = None
                        elif parent.value < current.value:
                            parent.right = None
                    else:
                        if parent == None:
                            self.root = current.left
                        elif parent.value > current.value:
                            parent.left = current.left
                        elif parent.value < current.value:
                            parent.right = current.left
                # Situation 2: node's right child has no left child
                elif current.right.left == None:
                    substitute = current.right
                    if substitute.left == None:
                        if parent == None:
                            self.root = substitute
                        elif parent.value > current.value:
                            parent.left = substitute
                        elif parent.value < current.value:
                            parent.right = substitute
                    substitute.left = current.left

                # Situation 3: node's right child has left child  
                else:
                    substitute = current.right.left
                    substituteParent = current.right
                    while(substitute.left != None):
                        substituteParent = substitute
                        substitute = substitute.left
                    if parent == None:
                        self.root = substitute
                    elif parent.value > current.value:
                        parent.left = substitute
                    elif parent.value < current.value:
                        parent.right = substitute
                    substituteParent.left = substitute.right
                    substitute.left = current.left
                    substitute.right = current.right

                
                del current
                return





bst = BST()

bst.insert(101)
bst.insert(33)
bst.insert(105)
bst.insert(9)
bst.insert(37)
bst.insert(104)
bst.insert(144)

# bst.traverseInOrder(bst.root)
# bst.traversePreOrder(bst.root)
# bst.traversePostOrder(bst.root)
bst.BFS()