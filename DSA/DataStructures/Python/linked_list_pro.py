from typing import Iterable
from linked_list import LinkedList
from node import Node
#from warnings import deprecated

class LinkedListPro(LinkedList):
    """Represents an advanced linked list"""
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
