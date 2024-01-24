class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_max_value_iterative(node):
    # Якщо дерево порожнє, повертаємо None
    if not node:
        return None

    # Починаємо з кореневого вузла
    current = node

    # спускаємося вправо до останнього правого вузла
    while current.right:
        current = current.right

    # Повертаємо значення останнього правого вузла
    return current.key


def create_sample_tree():
    # Створюємо дерево
    #      8
    #     / \
    #    3   10
    #   / \    \
    #  1   6    14
    #     / \   /
    #    4   7  13

    root = BinaryTreeNode(8)
    root.left = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(6)
    root.left.right.left = BinaryTreeNode(4)
    root.left.right.right = BinaryTreeNode(7)

    root.right = BinaryTreeNode(10)
    root.right.right = BinaryTreeNode(14)
    root.right.right.left = BinaryTreeNode(13)

    return root


if __name__ == "__main__":
    tree_root = create_sample_tree()

    max_value_iterative = find_max_value_iterative(tree_root)
    print(f"Найбільше значення в дереві: {max_value_iterative}")
