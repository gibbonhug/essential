from typing import Optional
from linked_list import Node

# Reverse Linked List
# Leetcode 206
# https://leetcode.com/problems/reverse-linked-list/

def reverse_linked_list_lc206(head: Optional[Node]) -> Optional[Node]:
    """Given the head of a singly linked list, reverse the list, and return the reversed list.

    Time complexity: O(n) [iterate over entire list]
    Space complexity: O(1)

    :param head: The head of the linked list to reverse
    :type head: Optional[Node]

    :rtype: Optional[Node]
    :return: The new head of the reverse linked list (tail of the old list)
    """
    prev_node: None
    this_node: ListNode = head

    while (this_node):
        temp_node = this_node.next
        this_node.next = prev_node

        prev_node = this_node
        this_node = temp_node
    
    # this_node will now be None and prev_node will now be old tail
    return prev_node 

def reverse_linked_list_recursive_lc206(head: Optional[Node]) -> Optional[Node]:
    """Given the head of a singly linked list, reverse the list, and return the reversed list.

    Recursive implementation

    Time complexity: O(n) [iterate over entire list]
    Space complexity: O(n) [recursive calls]

    :param head: The head of the linked list to reverse
    :type head: Optional[ListNode]

    :rtype: Optional[ListNode]
    :return: The new head of the reverse linked list (tail of the old list)
    """
    # head is None: nothing to reverse (passed empty list)
    if not head:
        return None
    
    new_head = head

    # if there are nodes after this node, reverse following portion of LL
    if head.next:
        new_head = reverse_linked_list_recursivelc206(head.next)
        # reversal
        head.next.next = head
    
    # on last call this will make original head of list be followed by None
    head.next = None 
    
    # on last call this will return original last node in list
    return new_head