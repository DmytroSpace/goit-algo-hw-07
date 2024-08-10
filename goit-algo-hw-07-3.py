class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_of_values(node):                                                  # Функція знаходження суми всіх значень у двійковому дереві пошуку
    if node is None:
        return 0                                                          # Повертаємо 0 для порожнього дерева

    left_sum = sum_of_values(node.left)                                   # Сума значень у лівому піддереві
    right_sum = sum_of_values(node.right)                                 # Сума значень у правому піддереві
    
    return node.key + left_sum + right_sum                                # Сума значень у корені та обох піддерев

if __name__ == '__main__':
    root = BinaryTreeNode(15)
    root.left = BinaryTreeNode(10)
    root.right = BinaryTreeNode(20)
    root.left.left = BinaryTreeNode(5)
    root.left.right = BinaryTreeNode(13)
    root.right.left = BinaryTreeNode(18)
    root.right.right = BinaryTreeNode(25)
    root.left.left.left = BinaryTreeNode(3)
    root.left.left.right = BinaryTreeNode(8)
    root.right.left.right = BinaryTreeNode(19)
    root.right.right.right = BinaryTreeNode(30)
    
    
    total_sum = sum_of_values(root)                                      # Знаходимо суми всіх значень
    print("Sum of all values:", total_sum)   
