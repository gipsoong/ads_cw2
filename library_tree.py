class Node:

    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def insert(self, key, value=None):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
                self.left.value = value
            else:
                self.left.insert(key, value)

        else:
            if self.right is None:
                self.right = Node(key)
                self.right.content = value
            else:
                self.right.insert(key, value)

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
