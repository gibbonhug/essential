from Implementations.linked_list import Node
from typing import Optional

# Reorder List
# Leetcode 143
# https://leetcode.com/problems/reorder-list/

def reorder_list_lc143(head: Optional[Node]) -> None:
    """
    Do not return anything, modify head in-place instead.

    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln

    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

    Time Complexity:
    Space Complexity:

    :param head: The head of the linked list to reorder
    :type head: Optional[Node]

    :rtype: None
    :return: None; modify head in-place
    """
    if not head:
        return