"""Count how many universal value trees exist within a given tree."""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_unival(root):

    if not root:
        return True

    if root.left != None and root.left.value != root.value:
        return False

    if root.right != None and root.right.value != root.value:
        return False

    if is_unival(root.left) and is_unival(root.right):
        return True
    return False


def count_univals(root):
    """Complexity is o(n^2)"""

    if not root:
        return 0

    total_count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        total_count += 1
    return total_count


tree = Node(value=1)
tree.left = Node(value=1)
tree.right = Node(value=0)
tree.right.left = Node(value=1)
tree.right.right = Node(value=0)
tree.right.right = Node(value=0)
tree.right.left.left = Node(value=1)
tree.right.left.right = Node(value=1)


print(count_univals(tree))

