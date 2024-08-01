class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n: int):
        if (self._size + n) > self._capacity:
            raise ValueError("Jar's capacity exceeded")
        self._size += n

    def withdraw(self, n: int):
        if n > self._size:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(1)
    print(jar)

if __name__ == "__main__":
    main()