from typing import override, Any
from linked_list import LinkedList
from node import Node

class Stack(LinkedList):
    """Represents a stack"""
    @override
    def push(self, value: Any):
        """Push a new value to the top of the stack"""
        new_head = Node(value)
        new_head.next = self._head
        self._head = new_head
        self._length += 1

    def __raise_if_empty(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

    def pop(self) -> Any:
        """Deletes and returns a value from the top of the stack"""
        self.__raise_if_empty()
        value = self._head.value
        self._head = self._head.next
        self._length -= 1
        return value

    def peek(self) -> Any:
        """Returns a value from the top of the stack"""
        self.__raise_if_empty()
        return self._head.value
