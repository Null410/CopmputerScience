from typing import Protocol, Any

class StructNode(Protocol):
    """Node Protocol"""
    @property
    def next(self) -> Any:
        """Returns the next node"""
    @property
    def value(self) -> Any:
        """Returns the value"""

class StructIterator:
    """Represents a struct iterator"""
    def __init__(self, head: StructNode | None):
        self.__head = head
    def __iter__(self):
        return self
    def __next__(self):
        if self.__head is None:
            raise StopIteration
        node = self.__head
        self.__head = self.__head.next
        return node.value
