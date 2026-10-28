from __future__ import annotations
from typing import Any, overload
import threading
import asyncio
from struct_interface import BaseStruct
from nodes.node import Node

class LinkedList(BaseStruct):
    """Represents a linked list"""
    def __init__(self, head: Node | None = None):
        self._head = head
        self._length = self.__calculate_len(head)
        self._lock = threading.Lock()
        self._async_lock = asyncio.Lock()

    @staticmethod
    def __calculate_len(head: Node| None) -> int:
        """Calculates and returns the length of the list"""
        leng = 0
        while head:
            leng += 1
            head = head.next
        return leng

    def _push(self, value: Any):
        """Push a new value to the end of the list"""
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            tail = self._head
            while tail.next:
                tail = tail.next
            tail.next = new_node
        self._length += 1

    def push(self, value: Any):
        """Push a new value to the end of the list. Thread-safe."""
        with self._lock:
            self._push(value)

    async def push_async(self, value: Any):
        """Push a new value to the end of the list. Asynchronous."""
        async with self._async_lock:
            self._push(value)

    def is_empty(self):
        """Returns True if list is empty and False if not"""
        return self._head is None

    def __len__(self):
        return self._length

    def __str__(self):
        result = f"[{len(self)}]: "
        if self.is_empty():
            return result
        tmp = self._head
        while tmp:
            result += f"{tmp.value} -> "
            tmp = tmp.next
        return result[:-4]

    def __iter__(self):
        return ListIterator(self._head)

    @overload
    def __getitem__(self, idx: int) -> Any:
        ...

    @overload
    def __getitem__(self, idx: slice) -> 'LinkedList':
        ...

    def __getitem__(self, idx: int | slice) -> Any | 'LinkedList':
        if isinstance(idx, slice):
            # may be implemented later
            raise NotImplementedError

        if idx < 0:
            leng = len(self)
            idx = leng + idx
            if idx < 0:
                raise IndexError

        node = self._head
        while node and idx >= 0:
            result = node.value
            node = node.next
            idx -= 1
        if idx >= 0:
            raise IndexError
        return result

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
