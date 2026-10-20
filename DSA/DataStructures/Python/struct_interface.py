from abc import ABC, abstractmethod
from typing import Any

class BaseStruct(ABC):
    """Base struct interface"""
    @abstractmethod
    def push(self, value: Any):
        """PUSH to the struct"""
        pass
    @abstractmethod
    def __len__(self): pass
    @abstractmethod
    def __str__(self): pass
    @abstractmethod
    def __iter__(self): pass

class Struct(BaseStruct):
    """Struct interface"""
    @abstractmethod
    def pop(self) -> Any:
        """POP from the struct"""
        pass
    @abstractmethod
    def peek(self) -> Any:
        """PEEK from the struct"""
        pass
