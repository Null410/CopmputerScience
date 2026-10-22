from typing import Any
import threading
import asyncio
from struct_interface import Struct
from doubly_node import DoublyNode
from linked_list import ListIterator

class Deque(Struct):
    """Represents a deque"""
    def __init__(self):
        self._head: DoublyNode = None
        self._tail: DoublyNode = None
        self._length = 0
        self._lock = threading.Lock()
        self._async_lock = asyncio.Lock()

    def is_empty(self):
        """Returns True if deque is empty and False if not"""
        return self._head is None

    def _push(self, value: Any):
        """Push a new value to the end of the deque"""
        new_node = DoublyNode(value)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = self._tail.next
        self._length += 1

    def push(self, value: Any):
        """Push a new value to the end of the deque. Thread-safe."""
        with self._lock:
            self._push(value)

    async def push_async(self, value: Any):
        """Push a new value to the end of the deque. Asynchronous."""
        async with self._async_lock:
            self._push(value)

    def __raise_if_empty(self):
        if self.is_empty():
            raise IndexError("Deque is empty")

    def _pop(self) -> Any:
        self.__raise_if_empty()
        value = self._head.value
        if self._head is self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._length -= 1
        return value

    def pop(self) -> Any:
        """Deletes and returns a value from the top of the deque. Thread-safe."""
        with self._lock:
            return self._pop()

    async def pop_async(self) -> Any:
        """Deletes and returns a value from the top of the deque. Asynchronous."""
        async with self._async_lock:
            return self._pop()

    def peek(self) -> Any:
        """Returns a value from the top of the deque"""
        self.__raise_if_empty()
        return self._head.value

    def __len__(self):
        return self._length

    def __str__(self):
        result = f"[{len(self)}]: "
        if self.is_empty():
            return result
        tmp = self._head
        while tmp:
            result += f"{tmp.value} <-> "
            tmp = tmp.next
        return result[:-5]

    def __iter__(self):
        return ListIterator(self._head)

    def __reversed__(self):
        node = self._tail
        while node:
            yield node.value
            node = node.prev
