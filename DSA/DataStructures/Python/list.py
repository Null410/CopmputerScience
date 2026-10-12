from __future__ import annotations
from typing import Any
#from warnings import deprecated

class Node:
    """Represents a node"""
    __slots__ = ['_value', '_next']
    def __init__(self, value: Any, next_node: 'Node' | None = None):
        self._value = value
        self._next = next_node
    @property
    def value(self):
        """Returns a value"""
        return self._value
    @value.setter
    def value(self, value: Any):
        self._value = value
    @property
    def next(self):
        """Returns a next node"""
        return self._next
    @next.setter
    def next(self, next_node: Node | None):
        self._next = next_node

class List:
    """Represents a linked list"""
    def __init__(self, head: Node | None = None):
        self._head = head
    @classmethod
    def from_values(cls, *args):
        """Returns a new list from args"""
        head = tail = None
        for arg in args:
            new_node = Node(arg)
            if head is None:
                head = new_node
                tail = head
            else:
                tail.next = new_node
                tail = tail.next
        return cls(head)

    @classmethod
    def from_iter_values(cls, *args):
        """
        Returns a new list from args.
        For nested iterable objects, each element of such an object becomes a node in the list.
        """
        if not args:
            return cls()

        tail: Node = None
        head: Node = None
        # Сlosure is used.
        def processing_iter(args) -> None:
            nonlocal tail
            nonlocal head
            if hasattr(args, '__iter__'):
                for arg in args:
                    processing_iter(arg)
            else:
                new_node = Node(args)
                if tail is None:
                    head = tail = new_node
                    return
                tail.next = new_node
                tail = tail.next

        processing_iter(args)
        return cls(head)

    #@deprecated("Use from_iter_values( *args) instead")
    @classmethod
    def from_iter_values_alternative_1(cls, *args):
        """
        An alternative function for from_iter_values(*args).
        Returns a new list from args.
        For nested iterable objects, each element of such an object becomes a node in the list.
        """
        if not args:
            return cls()
        # The function returns only a head node.
        # Repeated passage to the end of the list (tail) generated for each iterated object.
        def processing_iter(args) -> Node:
            if not hasattr(args, '__iter__'):
                return Node(args)
            head = tail = None
            for arg in args:
                tmp = processing_iter(arg)
                if head is None:
                    head = tmp
                else:
                    tail.next = tmp
                while tmp.next:
                    tmp = tmp.next
                tail = tmp
            return head

        return cls(processing_iter(args))

    #@deprecated("Use from_iter_values( *args) instead")
    @classmethod
    def from_iter_values_alternative_2(cls, *args):
        """
        An alternative function for from_iter_values(*args).
        Returns a new list from args.
        For nested iterable objects, each element of such an object becomes a node in the list.
        """
        if not args:
            return cls()
        # The function returns head and tail nodes (even if they are identical).
        def processing_iter(args) -> tuple[Node, Node]:
            if not hasattr(args, '__iter__'):
                new_node = Node(args)
                return (new_node, new_node)
            head = tail = None
            for arg in args:
                iter_head, iter_tail = processing_iter(arg)
                if head is None:
                    head = iter_head
                    tail = iter_tail
                    continue
                tail.next = iter_head
                tail = iter_tail
            return head, tail
        return cls(processing_iter(args)[0])

    def __str__(self):
        if self._head is None:
            return "None"
        result = ''
        tmp = self._head
        while tmp:
            result += f"{tmp.value} -> "
            tmp = tmp.next
        return result[:-4]
