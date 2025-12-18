from collections import deque
from typing import Any, Deque, Iterable


class Stack:
    """
    Простой стек (LIFO) на базе списка
    Вершина стека — правый край списка
    """

    def __init__(self, items: Iterable[Any] | None = None) -> None:
        """Можно инициализировать готовой последовательностью"""
        self._data: list[Any] = list(items) if items is not None else []

    def push(self, item: Any) -> None:
        """Добавляет элемент на вершину стека"""
        self._data.append(item)

    def pop(self) -> Any:
        """
        Снимает верхний элемент стека
        Поднимает IndexError, если стек пуст
        """
        if self.is_empty():
            raise IndexError("Невозможно выполнить pop: стек пуст")
        return self._data.pop()

    def peek(self) -> Any | None:
        """
        Возвращает верхний элемент без удаления
        Если стек пуст — None
        """
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """True, если стек пуст"""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


class Queue:
    """
    Очередь FIFO на базе collections.deque
    Голова очереди — левый край deque
    """

    def __init__(self, items: Iterable[Any] | None = None) -> None:
        """Можно инициализировать готовой последовательностью"""
        self._data: Deque[Any] = deque(items or [])

    def enqueue(self, item: Any) -> None:
        """Добавляет элемент в конец очереди"""
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Извлекает элемент из начала очереди
        Поднимает IndexError, если очередь пуста
        """
        if self.is_empty():
            raise IndexError("Невозможно выполнить dequeue: очередь пуста")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """
        Возвращает первый элемент без удаления
        Если очередь пуста — None
        """
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """True, если очередь пуста"""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)!r})"

