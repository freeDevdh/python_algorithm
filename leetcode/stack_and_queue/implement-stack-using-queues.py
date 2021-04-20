'''
큐를 이용하여 스택을 구현하라
-push(x) : 요소 x를 스택에 삽입한다.
-pop() : 스택의 첫 번째 요소를 삭제한다.
-top() : 스택의 첫 번째 요소를 가져온다.
-empty() : 스택이 비어 있는지 여부를 판단한다.
'''
import collections


class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        # 요소를 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()