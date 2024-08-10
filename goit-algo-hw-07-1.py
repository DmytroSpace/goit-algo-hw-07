import matplotlib.pyplot as plt
import networkx as nx

class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_value(node):                          # Функція для знаходження найбільшого значення у бінарному дереві пошуку
    if node is None:
        raise ValueError("Tree is empty")          # Перевяємо чи є дерево порожнім
        
    current = node
    while current.right is not None:               # Перебираємо усі праві вузли, доки не дійдемо до найправішого з найбільшим значенням
        current = current.right
    return current.key


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
    
    
    max_value = find_max_value(root)               # Знаходимо максимальне значення:
    print("Maximum value:", max_value) 
    
