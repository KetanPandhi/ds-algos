from q import Queue


class Node:

    def __init__(self, value: int, parent_node=None, left_node=None, right_node=None):
        self.value = value
        self.parent = parent_node
        self.left = left_node
        self.right = right_node


class BST:

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, val):
        if self.root:
            self._put(self.root, val)
        else:
            self.root = Node(val)
        self.size += 1

    def _put(self, current_node, val):
        if val < current_node.value:
            if current_node.left:
                self._put(current_node.left, val)
            else:
                current_node.left = Node(val, current_node)
        else:
            if current_node.right:
                self._put(current_node.right, val)
            else:
                current_node.right = Node(val, current_node)

    def get(self, val):
        if self.root:
            return self._get(self.root, val)
        else:
            return None

    def _get(self, current_node, val):
        if not current_node:
            return None
        elif current_node.value == val:
            return current_node
        elif val < current_node.value:
            return self._get(current_node.left, val)
        else:
            return self._get(current_node.right, val)

    def level_order_traversal(self):
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.isEmpty():
            current_node = queue.dequeue()
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            print(current_node.value)

    def inorder(self):
        if self.root:
            self._inorder(self.root)

    def _inorder(self, current_node):
        if not current_node:
            return
        else:
            self._inorder(current_node.left)
            print(current_node.value)
            self._inorder(current_node.right)

    def preorder(self):
        if self.root:
            self._preorder(self.root)

    def _preorder(self, current_node):
        if not current_node:
            return
        else:
            print(current_node.value)
            self._preorder(current_node.left)
            self._preorder(current_node.right)

    def postorder(self):
        if self.root:
            self._postorder(self.root)

    def _postorder(self, current_node):
        if not current_node:
            return
        else:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(current_node.value)


bst = BST()

bst.put(5)
bst.put(3)
bst.put(8)
bst.put(4)
bst.put(1)
bst.put(7)
bst.put(9)

bst.level_order_traversal()
print("-------------------")
bst.preorder()
print("-------------------")
bst.inorder()
print("-------------------")
bst.postorder()
