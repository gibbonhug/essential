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

# Singly-linked single-ended linked list
class LinkedList:
    """
    Singly-linked single-ended linked list (with int data)

    ...

    Attributes
    ----------
    head : Node
        head node of the linked list

    Methods
    -------
    - prepend(node):
        Insert a node as a new head node of the list, and return the new head
    - append(node):
        Insert a node as the new tail node of the list, returning the new tail
    - add_as_head(value):
        Insert an int value as a new head node of the list, and return the new head
    - add(value):
        Insert an int value as the new tail node of the list, returning the new tail
    - shift():
        Remove and return the head of the linked list
    - decapitate():
        Same as shift()
    - pop():
        Remove and return the tail of the linked list
    - get_head():
        Get the head node of the list
    - get_tail():
        Get the tail node of the list
    - search(value):
        Returns a bool of whether int value appears as data within list
    - length():
        Get the number of nodes in the linked list
    - is_empty():
        Boolean value of whether the linked list is empty (contains 0 nodes)
    """
    def __init__(self, head: Optional[Node]):
        self.head = head

    def prepend(self, node: Node) -> Node:
        node.next = self.head

        self.head = node

        return node

    def append(self, node: Node) -> Node:
        if self.is_empty():
            return self.prepend(value)

        node.next = None

        old_tail: Node = self.get_tail()
        
        old_tail.next = node

        return node

    def add_as_head(self, value: int) -> Node:
        return prepend(Node(value))

    def add(self, value: int) -> Node:
        return append(Node(value))

    def shift(self) -> Optional[Node]:
        if self.is_empty():
            return None

        old_head: Node = self.head

        self.head = old_head.next

        return old_head

    def decapitate(self) -> Optional[Node]:
        return self.shift()

    def pop(self) -> Optional[Node]:
        if self.is_empty():
            return None

        old_tail: Node = self.get_tail()
        curr_node = self.head

        while curr_node.next != old_tail:
            curr_node = curr_node.next

        curr_node.next = None

        return old_tail

    def get_head(self) -> Optional[Node]:
        return self.head

    def get_tail(self) -> Optional[Node]:
        if self.is_empty():
            return None

        curr_node: Node = self.head

        while curr_node and curr_node.next:
            curr_node = curr_node.next

        return curr_node

    def search(self, value) -> bool:
        if self.is_empty():
            return False

        curr_node: Node = self.head

        while curr_node:
            if curr_node.data == value:
                return True

            curr_node = curr_node.next

        # Searched entire list
        return False
        

    def length(self) -> int:
        length: int = 0

        curr_node: Node = self.head

        while curr_node:
            curr_node = curr_node.next
            length += 1

        return length

    def is_empty(self) -> bool:
        return False if self.head else True

    def __str__(self):
        curr_node: Node = self.head
        strings = []

        while curr_node:
            strings.append(str(curr_node))
            curr_node = curr_node.next
        
        return ("".join(strings))
