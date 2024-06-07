
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
