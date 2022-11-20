from typing import Optional

# Invert Binary Tree
# Leetcode 226
# https://leetcode.com/problems/invert-binary-tree/

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

    Time complexity: O(n), n == number of nodes
    Space complexity: O(h), h == height of tree (?)

    :param root: The root node of the binary tree to invert
    :type root: Optional[TreeNode]

    :rtype: int
    :return: The diameter of the binary tree
    """
    diam: int = 0

    def height_of_node(root: Optional[TreeNode]) -> int:
        nonlocal diam 

        if not root:
            return 0

        left_hite: int = height_of_node(root.left)
        rite_hite: int = height_of_node(root.right)

        # update diameter
        diam = max(diam, left_hite + rite_hite)

        # return height of this node
        return 1 + max(left_hite, rite_hite)
    
    height_of_node(root)

    return diam
    