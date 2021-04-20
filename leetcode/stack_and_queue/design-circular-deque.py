'''
원형 데크를 디자인하라.
'''


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.deque = []
        self.front = -1
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.insert(0, value)
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear += 1
        self.deque.append(value)
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop(0)
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True

    def isEmpty(self) -> bool:
        return len(self.deque) == 0
    def isFull(self) -> bool:
        return self.size == len(self.deque)

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