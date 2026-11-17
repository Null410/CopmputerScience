from nodes.node import Node
from nodes.doubly_node import DoublyNode

#! Will be changed to work correctly with different Node types and values
class StructIterator:
    """Represents a linked list iterator"""
    def __init__(self, head: Node | DoublyNode | None):
        self.__head = head
    def __iter__(self):
        return self
    def __next__(self):
        if self.__head is None:
            raise StopIteration
        node = self.__head
        self.__head = self.__head.next
        return node.value
