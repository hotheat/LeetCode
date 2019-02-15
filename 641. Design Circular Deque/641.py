from itertools import chain


class MyCircularDeque:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capicity = k + 1
        self.items = [True] * self.capicity
        self.head, self.tail = 0, 0

    def insertFront(self, value: 'int') -> 'bool':
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.head = self.head - 1 if self.head != 0 else self.capicity - 1
            self.items[self.head] = value
            return True
        else:
            return False

    def insertLast(self, value: 'int') -> 'bool':
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.capicity
            return True
        else:
            return False

    def deleteFront(self) -> 'bool':
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.items[self.head] = True
            self.head = (self.head + 1) % self.capicity
            return True
        else:
            return False

    def deleteLast(self) -> 'bool':
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.tail = self.tail - 1 if self.tail != 0 else self.capicity - 1
            self.items[self.tail] = True
            return True
        else:
            return False

    def getFront(self) -> 'int':
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            item = self.items[self.head]
            return item
        else:
            return -1

    def getRear(self) -> 'int':
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            tail = self.tail - 1 if self.tail != 0 else self.capicity - 1
            item = self.items[tail]
            return item
        else:
            return -1

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular deque is empty or not.
        """
        if self.head == self.tail:
            print('the queue is empty')
            return True
        else:
            return False

    def isFull(self) -> 'bool':
        """
        Checks whether the circular deque is full or not.
        """
        if (self.tail + 1) % self.capicity == self.head:
            print('the queue is full')
            return True
        else:
            return False

    def __repr__(self):
        if self.head < self.tail:
            return ' '.join((str(i) for i in self.items[self.head:self.tail]))
        elif self.head > self.tail:
            return ' '.join(str(i) for i in chain(self.items[self.head:], self.items[:self.tail]))
        else:
            return ''


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

if __name__ == '__main__':
    obj = MyCircularDeque(3)
    print(obj.insertLast(1))
    print(obj.insertLast(2))
    print(obj.insertFront(3))
    print(obj.insertFront(4))
    print(obj.getRear())
    print(obj.isFull())
    print(obj.deleteLast())
    print(obj.insertFront(4))
    print(obj.getFront())
    print(obj)
