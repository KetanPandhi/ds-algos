

class Double_Node:
    def __init__(self, val):
        self.next = None
        self.previous = None
        self.val = val


class Doubly_Linked_List:

    head = None
    tail = None

    def add(self, val):
        new_node = Double_Node(val)
        new_node.previous = self.tail
        if not self.head:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
