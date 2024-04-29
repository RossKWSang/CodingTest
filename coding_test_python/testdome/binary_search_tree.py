class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def contains(self, root, value):
        if not root:
            return False

        if root.value == value:
            return True
        elif root.value > value:
            return self.contains(root.left, value)
        else:
            return self.contains(root.right, value)

    def main(self):
        n1 = Node(1, None, None)
        n3 = Node(3, None, None)
        n2 = Node(2, n1, n3)

        print(self.contains(n2, 3))


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.main()
