from typing import Any
from node import Node

class LinkedList:
    """Represents a linked list"""
    def __init__(self, head: Node | None = None):
        self._head = head

    @property
    def length(self) -> int:
        """Calculates and returns the length of the list"""
        leng = 0
        node = self._head
        while node:
            leng += 1
            node = node.next
        return leng

    def push(self, value: Any):
        """Push a new value to the end of the list"""
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
            return
        tail = self._head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def is_empty(self):
        """Returns True if list is empty and False if not"""
        return self._head is None

    def __str__(self):
        if self.is_empty():
            return "None"
        result = ''
        tmp = self._head
        while tmp:
            result += f"{tmp.value} -> "
            tmp = tmp.next
        return result[:-4]

    def __len__(self):
        return self.length

    def __iter__(self):
        return ListIterator(self._head)

class ListIterator:
    """Represents a linked list iterator"""
    def __init__(self, head: Node):
        self.__head = head
    def __iter__(self):
        return self
    def __next__(self):
        if self.__head is None:
            raise StopIteration
        node = self.__head
        self.__head = self.__head.next
        return node.value
