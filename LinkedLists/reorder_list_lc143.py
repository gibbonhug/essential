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

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param head: The head of the linked list to reorder
    :type head: Optional[Node]

    :rtype: None
    :return: None; modify head in-place
    """
    if not head:
        return

    # Problem is essentially combination of finding middle of a LL, 
    # reversing a LL, and merging two LL in a set pattern

    # Find middle of the linked list / start of second half
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next # After while loop ends, slow will hold end of 1st half
        fast = fast.next.next

    # Reverse second half of LL, first detaching it
    this_node = slow.next
    slow.next = None # Detach second half from first half
    prev_node = None

    while this_node:
        temp_node = this_node.next
        this_node.next = prev_node

        prev_node = this_node
        this_node = temp_node

    # prev_node now holds head of reversed detached 2nd half

    # Intersperse the 2 lists
    l1 = head
    l2 = prev_node

    while l2:
        old_l1_next = l1.next
        old_l2_next = l2.next

        l1.next = l2
        l2.next = old_l1_next

        l1 = old_l1_next
        l2 = old_l2_next