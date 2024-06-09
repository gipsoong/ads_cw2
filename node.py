class Node:

    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def insert(self, key, value=None):
        if key < self.key:
            if self.left is None:
                self.left = Node(key, value)
                self.left.value = value
            else:
                self.left.insert(key, value)

        else:
            if self.right is None:
                self.right = Node(key, value)
                self.right.value = value
            else:
                self.right.insert(key, value)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)

        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.value)

    def find(self, key):
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(key)

        elif key > self.key:
            if self.right is None:
                return None
            else:
                return self.right.find(key)
        else:
            return self
