class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        pass
        if self.left:
            self.left.inorder_traversal()
        print(self.value)

        if self.right:
            self.right.inorder_traversal()

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)

        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True