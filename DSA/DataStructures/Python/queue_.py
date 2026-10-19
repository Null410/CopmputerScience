from typing import override, Any
from linked_list import LinkedList
from node import Node

class Queue(LinkedList):
    """Represents a queue"""
    def __init__(self):
        self._tail: Node = None
        super().__init__()

    @override
    def push(self, value: Any):
        """Push a new value to the end of the queue"""
        node = Node(value)
        if self.is_empty():
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self._length += 1

    def __raise_if_empty(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

    def pop(self) -> Any:
        """Deletes and returns a value from the top of the queue"""
        self.__raise_if_empty()
        value = self._head.value
        if self._tail is self._head:
            self._tail = None
        self._head = self._head.next
        self._length -= 1
        return value

    def peek(self) -> Any:
        """Returns a value from the top of the queue"""
        self.__raise_if_empty()
        return self._head.value
