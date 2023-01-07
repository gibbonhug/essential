from Implementations.linked_list import Node
from typing import Optional

# Linked List Cycle
# Leetcode 141
# https://leetcode.com/problems/linked-list-cycle/

def linked_list_cycle_lc141(head: Optional[Node]) -> bool:
    """Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.
    
    Time Complexity: O(n)
    Space Complexity: O(1)

    :param head: The head of the linked list, if it exists
    :type head: Optional[Node]

    :rtype: bool
    :return: Whether the list referred to by head contains a cycle
    """
    if not head:
        return False

    slow: Node = head
    fast: Node = head

    while fast and fast.next:
        # Advance pointers
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    # Successfully exited list: no cycle exists
    return False