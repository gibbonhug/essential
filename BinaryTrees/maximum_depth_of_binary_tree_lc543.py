# Invert Binary Tree
# Leetcode 226
# https://leetcode.com/problems/invert-binary-tree/

# unfinished

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maximum_depth_of_binary_tree_lc104(root: Optional[TreeNode]) -> int:
   """Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.

    :param root: The root node of the binary tree to invert
    :type root: Optional[TreeNode]

    :rtype: int
    :return: The maximum diam
    """