from typing import Any, Callable
import threading
import asyncio
from structs.struct_interface import Struct
from structs.struct_iterator import StructIterator
from nodes.doubly_node import DoublyNode

class Deque(Struct):
    """Represents a deque"""

    def __init__(self):
        self._head: DoublyNode | None = None
        self._tail: DoublyNode | None = None
        self._length = 0
        self._lock = threading.Lock()
        self._async_lock = asyncio.Lock()

    def is_empty(self):
        """Returns True if deque is empty and False if not"""
        return self._head is None

    def _push(self, value: Any):
        """Push a new value to the end of the deque"""
        new_node = DoublyNode(value)
        if self._tail is None: # _head is None
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

    def __raise_if_empty(self) -> DoublyNode:
        if self._head is None:
            raise IndexError("Deque is empty")
        return self._head

    def _pop(self) -> Any:
        head = self.__raise_if_empty()
        value = head.value
        self._head = head.next
        if self._head is None:
            self._tail = None
        else:
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
        head = self.__raise_if_empty()
        return head.value

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
        return StructIterator(self._head)

    def __reversed__(self):
        node = self._tail
        while node:
            yield node.value
            node = node.prev

    def __getitem__(self, idx: int) -> Any:
        leng = len(self)
        if idx < 0:
            idx = leng + idx
            if idx < 0:
                raise IndexError
        else:
            if idx >= leng:
                raise IndexError

        get_next: Callable[[DoublyNode], DoublyNode | None]
        node: DoublyNode | None

        if idx <= leng // 2:
            def next_(node: DoublyNode):
                return node.next
            node = self._head
            get_next = next_
        else:
            def prev_(node: DoublyNode):
                return node.prev
            idx = leng - idx - 1
            node = self._tail
            get_next = prev_

        while node and idx >= 0:
            result = node.value
            node = get_next(node)
            idx -=1
        #if idx >= 0:
        #    raise IndexError
        return result
