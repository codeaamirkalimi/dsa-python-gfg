class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        print(self.data)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    def insertTree(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertTree(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertTree(data)


root = Node(10)
root.insertTree(2)
root.insertTree(40)
root.insertTree(5)
root.insertTree(42)
root.insertTree(1)
root.insertTree(0)
root.printTree()
