from typing import Any, Iterable
from node import Node
#from warnings import deprecated

class LinkedList:
    """Represents a linked list"""
    def __init__(self, head: Node | None = None):
        self._head = head

    @property
    def length(self) -> int:
        """Calculates and returns the length of the list"""
        leng = 0
        node = self._head
        while node:
            leng += 1
            node = node.next
        return leng

    def push(self, value: Any):
        """Push a new value to the end of the list"""
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            return
        tail = self._head
        while tail.next:
            tail = tail.next
        tail.next = new_node

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
    def from_iterable(cls, iterable: Iterable):
        """Returns a new list from iterable"""
        head = None
        tail = None

        for item in iterable:
            node = Node(item)
            if head is None:
                head = tail = node
                continue
            tail.next = node
            tail = tail.next
        return cls(head)

    @classmethod
    def from_iter_values(cls, *args):
        """
        Returns a new list from args.
        For nested iterable objects, each element of such an object becomes a node in the list.
        For strings (as well as str instances): each of their characters also becomes a list node.
        *Example:
            Input data: ( 1, [2, 3], 4, [5, ['67', 8], 9], 10 )
            LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> '6' -> '7' -> 8 -> 9 -> 10
        !Attention:
            In the case of an infinite iteration, the method raises a RecursionError exception
            (for example, when the iterable object contains a reference to itself).
        """
        if not args:
            return cls()

        tail: Node = None
        head: Node = None
        # Сlosure is used.
        def processing_iter(args) -> None:
            nonlocal tail
            nonlocal head
            if not hasattr(args, '__iter__') or (isinstance(args, str) and len(args) == 1):
                new_node = Node(args)
                if tail is None:
                    head = tail = new_node
                    return
                tail.next = new_node
                tail = tail.next
            else:
                for arg in args:
                    processing_iter(arg)

        processing_iter(args)
        return cls(head)

    #@deprecated("Use from_iter_values( *args) instead")
    @classmethod
    def from_iter_values_alternative_1(cls, *args):
        """
        An alternative function for from_iter_values(*args).
        """
        if not args:
            return cls()
        # The function returns only a head node.
        # Repeated passage to the end of the list (tail) generated for each iterated object.
        def processing_iter(args) -> Node:
            if not hasattr(args, '__iter__') or (isinstance(args, str) and len(args) == 1):
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
        """
        if not args:
            return cls()
        # The function returns head and tail nodes (even if they are identical).
        def processing_iter(args) -> tuple[Node, Node]:
            if not hasattr(args, '__iter__') or (isinstance(args, str) and len(args) == 1):
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

    def __iter__(self):
        return ListIterator(self._head)

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
