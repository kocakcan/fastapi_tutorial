# from typing import TypeVar, Generic
#
# T = TypeVar('T')
#
# class Stack(Generic[T]):
#     def __init__(self) -> None:
#         self._items: list[T] = []
#
#     def push(self, item: T) -> None:
#         self._items.append(item)
#
#     def pop(self) -> T:
#         self._items.pop()
#
# def first(items: list[T]) -> T:
#     return items[0]

class Stack[T]:
    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

def first[T](items: list[T]) -> T:
    return items[0]

def main():
    s: Stack[int] = Stack()
    items: list[str] = ["rug", "mug", "Pug"]
    items_2: list[int] = list(range(0, 10))
    s.push(1)
    s.push('x')
    print(f"First: {first(items)}")
    print(f"First: {first(items_2)}")

if __name__ == "__main__":
    main()
