from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        self._items.pop()

def main():
    s: Stack[int] = Stack()
    s.push(1)
    s.push('x')

if __name__ == "__main__":
    main()
