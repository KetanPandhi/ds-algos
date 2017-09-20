

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class Linked_List:

    head = None
    tail = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

    def display(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def reverse(self):

        curr = self.head
        tmp = None
        while curr:
            nn = curr.next
            curr.next = tmp
            tmp = curr
            curr = nn

        self.head = tmp


a = Linked_List()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.display()
a.reverse()
a.display()
