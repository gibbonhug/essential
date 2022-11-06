from typing import Optional

class Node:
    """
    A class used to represent a singly-linked Node with integer data

    ...

    Attributes
    ----------
    data : int
        int data stored in this node (default is 0)
    next : Node | None (optional)
        the next node, if it exists (default is None)
    """
    def __init__(self, data: int = 0, next = None):
         self.data = data
         self.next = next

    def __str__(self):
        if self.next:
            return f"({self.data}) -> "
        else:
            return f"({self.data})"

# Singly-linked single-ended linked list which rememebers its length
class LinkedList:
    """
    Singly-linked single-ended linked list (with int data) which rememebers its length

    ...

    Attributes
    ----------
    head : Node
        head node of the linked list
    length : int
        how many nodes the linked list holds

    Methods
    -------
    add_at_beginning(new_head):
        add a new head to the list, and return the new head

    remove_first_node():
        remove the current head of the list, and return the new head if it exists

    calc_length():
        manually calculate and return length of the list
    """
    def __init__(self, head: Node):
        self.head = head
        self.length = self.calc_length()

    def add_at_beginning(self, new_head: Node) -> Node:
        new_head.next = self.head
        self.head = new_head

        self.length += 1

        return new_head

    def remove_first_node(self) -> Optional[Node]:
        if (self.head):
            self.head = self.head.next

            self.length -= 1

            return self.head
        
        return None

    def calc_length(self) -> int:
        length = 0
        curr_node = self.head

        while (curr_node):
            length += 1
            curr_node = curr_node.next

        return length

    def __str__(self):
        curr_node = self.head
        strings = []

        while curr_node:
            strings.append(str(curr_node))
            curr_node = curr_node.next
        
        return ("".join(strings))
