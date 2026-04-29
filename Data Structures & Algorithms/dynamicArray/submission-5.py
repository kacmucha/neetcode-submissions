class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        res = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return res

    def resize(self) -> None:
        self.array.extend([None] * self.capacity)
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity