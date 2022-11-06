from linked_list import Node
from typing import Optional

# Middle Of The Linked List
# Leetcode 21
# https://leetcode.com/problems/merge-two-sorted-lists/

def merge_two_lists_lc21(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    """You are given the heads of two sorted linked lists list1 and list2. [Lists may be empty.]

    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    :param list1: The head of the first linked list
    :type list1: Optional[Node]
    :param list2: The head of the second linked list
    :type list2: Optional[Node]

    :rtype: Optional[Node]
    :return: The head of the merged list
    """
    fake_head: Node = Node() # account for empty list/s
    curr_node_new_list: Node = fake_head

    while list1 and list2:
        if list1.val < list2.val:
            curr_node_new_list.next = list1
            list1 = list1.next
        else:
            curr_node_new_list.next = list2
            list2 = list2.next
        # update curr_node_new_list to override on next loop
        curr_node_new_list = curr_node_new_list.next


    # fill remaining values
    if list1:
        curr_node_new_list.next = list1

    if list2:
        curr_node_new_list.next = list2

    return fake_head.next # decapitate the false head