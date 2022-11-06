from linked_list import Node

# Middle Of The Linked List
# Leetcode 806
# https://leetcode.com/problems/middle-of-the-linked-list/

def middle_of_the_linked_list_lc806(head: Node) -> Node:
    """Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    :param head: The head of the linked list
    :type head: Node

    :rtype: Node
    :return: The middle node of the linked list
    """
    slow_node: Node = head
    fast_node: Node = head

    while fast_node and fast_node.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    
    return slow_node 