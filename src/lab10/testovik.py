from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList


def main() -> None:
    print("Stack")
    stack = Stack([1, 2, 3, 4])
    print(f"Снятие верхнего элемента стека : {stack.pop()}")
    print(f"Пустой ли стек? {stack.is_empty()}")
    print(f"Число сверху : {stack.peek()}")
    stack.push(1)
    print(f"Значение сверху после добавления числа в стек : {stack.peek()}")
    print(f"Длина стека : {len(stack)}")
    print(f"Стек : {stack._data}")

    print("\nDeque")
    q = Queue([1, 2, 3, 4])
    print(f"Значение первого элемента : {q.peek()}")
    q.dequeue()
    print(f"Значение первого элемента после удаления числа : {q.peek()}")
    q.enqueue(52)
    print(f"Значение первого элемента после добавления числа : {q.peek()}")
    print(f"Пустая ли очередь? {q.is_empty()}")
    print(f"Количество элементов в очереди : {len(q)}")

    print("\nSinglyLinkedList")
    sll = SinglyLinkedList()
    print(f"Длина нашего односвязанного списка : {len(sll)}")

    sll.append(1)
    sll.append(2)
    sll.prepend(0)
    print(f"Наша нынешняя длина списка после добавления элементов : {len(sll)}")
    print(f"Односвязаный список : {list(sll)}")

    sll.insert(1, 0.5)
    print(f"Длина списка после добавления на 1 индекс числа 0.5 : {len(sll)}")
    print(f"Односвязаный список : {list(sll)}")
    sll.append(52)
    print(f"Односвязанный список после добавления числа в конец : {list(sll)}")

    print(sll)


if __name__ == "__main__":
    main()

