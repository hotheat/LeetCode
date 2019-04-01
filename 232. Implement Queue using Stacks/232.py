class MyQueue(object):
    """
    用栈来实现队列
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        if self.out_stack != []:
            return self.out_stack.pop()
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.out_stack == []:
            while self.in_stack != []:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.in_stack == [] and self.out_stack == []


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    # q.push(2)
    # print(q.peek())
    print(q.pop())
    print(q.empty())
    # print(q.pop())
    # print(q.pop())
