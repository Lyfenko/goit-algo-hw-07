class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_min_value_iterative(node):
    # Якщо дерево порожнє, повертаємо None
    if not node:
        return None

    # спускаємося вліво до останнього лівого вузла
    current = node
    while current.left:
        current = current.left

    # Повертаємо значення останнього лівого вузла
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

    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)

    root.right = TreeNode(10)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)

    return root


if __name__ == "__main__":
    tree_root = create_sample_tree()

    min_value_iterative = find_min_value_iterative(tree_root)
    print(f"Найменше значення в дереві: {min_value_iterative}")
