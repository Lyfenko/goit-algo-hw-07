class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_tree_sum(node):
    if not node:
        return 0

    # Знаходимо суму значень у лівому та правому піддеревах, додаємо поточне значення
    left_sum = find_tree_sum(node.left)
    right_sum = find_tree_sum(node.right)

    return node.key + left_sum + right_sum


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

    tree_sum = find_tree_sum(tree_root)
    print(f"Сума значень у дереві: {tree_sum}")
