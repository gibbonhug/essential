from typing import Optional

# Reverse Linked List
# Leetcode 206
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def reverse_linked_listlc206(head: Optional[ListNode]) -> Optional[ListNode]:
    """Given the head of a singly linked list, reverse the list, and return the reversed list.

    :param head: The head of the linked list to reverse
    :type head: Optional[ListNode]

    :rtype: Optional[ListNode]
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

def reverse_linked_list_recursivelc206(head: Optional[ListNode]) -> Optional[ListNode]:
    """Given the head of a singly linked list, reverse the list, and return the reversed list.

    Recursive implementation

    :param head: The head of the linked list to reverse
    :type head: Optional[ListNode]

    :rtype: Optional[ListNode]
    :return: The new head of the reverse linked list (tail of the old list)
    """
    