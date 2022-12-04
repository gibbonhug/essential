from typing import Optional

# unfinished (add more ways to solve)

# Invert Binary Tree
# Leetcode 226
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def invert_binary_tree_lc226_recursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Given the root of a binary tree, invert the tree, and return its root.

    :param root: The root node of the binary tree to invert
    :type root: Optional[TreeNode]

    :rtype: Optional[TreeNode]
    :return: The root node of the binary tree
    """
    if root is None:
        return None

    temp_node: Optional[TreeNode] = root.left
    root.left = root.right
    root.right = temp_node

    # recursively invert child nodes
    invert_binary_tree_recursive_lc226(root.left)
    invert_binary_tree_recursive_lc226(root.right)

    return root
    
