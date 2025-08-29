class Jar:
    def __init__(self, capacity=12):
        # Private variables
        self._capacity = 0
        self._size = 0

        self.capacity = capacity

    def __str__(self):
        return '🍪' * self._size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError(f'Depositing {n} would exceed the Jar capacity of {self.capacity}')

        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError(f'Withdrawing {n} would cause a negative balance')

        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError(f'Capacity of {value} is invalid')
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


def main():
    value = input('Enter something: ')


if __name__ == '__main__':
    main()
