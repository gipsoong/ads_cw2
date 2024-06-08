class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)

        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

    def inorder_traversal(self):
        pass
        if self.left:
            self.left.inorder_traversal()
        print(self.key)

        if self.right:
            self.right.inorder_traversal()

    def find(self, key):
        if key < self.key:
            if self.left is None:
                return False
            else:
                return self.left.find(key)

        elif key > self.key:
            if self.right is None:
                return False
            else:
                return self.right.find(key)
        else:
            return True
