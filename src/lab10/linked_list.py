from typing import Any, Iterator, Optional


class Node:
    """Узел односвязного списка"""

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


class SinglyLinkedList:
    """
    Односвязный список
    Поддерживает добавление в конец или вначало, вставку по индексу и удаление по индексу
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка за O(1) с учётом tail"""
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None  # для типа
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка за O(1)"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по индексу
        Допустимы idx == 0 (в начало) и idx == len(list) (в конец)
        """
        if idx < 0 or idx > self._size:
            raise IndexError("Индекс вне диапазона")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        prev = self._node_at(idx - 1)
        new_node = Node(value, next=prev.next)
        prev.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу. Поднимает IndexError при неверном индексе"""
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            assert self.head is not None
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        prev = self._node_at(idx - 1)
        assert prev.next is not None
        to_remove = prev.next
        prev.next = to_remove.next
        if prev.next is None:
            self.tail = prev
        self._size -= 1

    def _node_at(self, idx: int) -> Node:
        """Возвращает узел по индексу"""
        current = self.head
        for _ in range(idx):
            assert current is not None  # для mypy/pyright
            current = current.next
        assert current is not None
        return current

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = ", ".join(repr(v) for v in self)
        return f"SinglyLinkedList([{values}])"

