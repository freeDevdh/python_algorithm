'''
스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
- push(x) : 요소 x를 큐 마지막에 삽입힌다.
- pop() : 큐 처음에 있는 요소를 제거한다.
- peek() : 큐 처음에 있는 요소를 조회한다.
- empty() : 큐가 비어 있는지 여부를 리턴한다.
'''


class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []


    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()