from typing import override, Any
from structs.linked_list import LinkedList
from structs.struct_interface import Struct
from nodes.node import Node

class Queue(LinkedList, Struct):
    """Represents a queue"""
    def __init__(self):
        self._tail: Node | None = None
        super().__init__()

    @override
    def _push(self, value: Any):
        """Push a new value to the end of the queue"""
        node = Node(value)
        if self._tail is None: # _head is None
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self._length += 1

    def __raise_if_empty(self) -> Node:
        if self._head is None:
            raise IndexError("Queue is empty")
        return self._head

    def _pop(self) -> Any:
        """Deletes and returns a value from the top of the queue"""
        head = self.__raise_if_empty()
        value = head.value
        self._head = head.next
        if self._head is None:
            self._tail = None
        self._length -= 1
        return value

    def pop(self) -> Any:
        """Deletes and returns a value from the top of the queue. Thread-safe."""
        with self._lock:
            return self._pop()

    async def pop_async(self) -> Any:
        """Deletes and returns a value from the top of the queue. Asynchronous."""
        async with self._async_lock:
            return self._pop()

    def peek(self) -> Any:
        """Returns a value from the top of the queue"""
        head = self.__raise_if_empty()
        return head.value
