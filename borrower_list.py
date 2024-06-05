class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class BorrowerList:
    def __init__(self):
        self.start_node = None

    def insert_to_empty_list(self, value):
        if self.start_node is None:
            new_node = Node(value)
            self.start_node = new_node
        else:
            return "BorrowerList is empty"

    def insert_to_end(self, value):
        if self.start_node is None:
            new_node = Node(value)
            self.start_node = new_node
            return

        n = self.start_node
        while n.next is not None:
            n = n.next

        new_node = Node(value)
        n.next = new_node
        new_node.prev = n

    def return_borrower_list(self):
        if self.start_node is None:
            return "BorrowerList is empty"
        else:
            n = self.start_node
            while n is not None:
                print(f"Element is: {n.value}")
                n = n.next
