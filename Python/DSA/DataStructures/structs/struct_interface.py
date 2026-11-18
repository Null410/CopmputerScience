from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any, Iterator

class BaseStruct(Sequence, ABC):
    """Base struct interface"""
    @abstractmethod
    def push(self, value: Any):
        """PUSH to the struct"""
    @abstractmethod
    def __len__(self) -> int: ...
    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def __iter__(self) -> Iterator[Any]: ...
    @abstractmethod
    def __getitem__(self, key) -> Any: ...

class Struct(BaseStruct):
    """Struct interface"""
    @abstractmethod
    def pop(self) -> Any:
        """POP from the struct"""
    @abstractmethod
    def peek(self) -> Any:
        """PEEK from the struct"""
