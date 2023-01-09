from Implementations.linked_list import Node

# Basic task: Find the middle node of a linked list with the fast/slow 2-ptr technique

# Middle Of The Linked List
# Leetcode 806
# https://leetcode.com/problems/middle-of-the-linked-list/

def middle_of_the_linked_list_lc806(head: Node) -> Node:
    """Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    Time complexity: O(n) [iterate over entire list]
    Space complexity: O(1)

    :param head: The head of the linked list
    :type head: Node

    :rtype: Node
    :return: The middle node of the linked list
    """
    slow_node: Node = head
    fast_node: Node = head

    # once the pointer advancing twice as fast hits the end of the list, the slower will be at the middle
    while fast_node and fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    
    return slow_node