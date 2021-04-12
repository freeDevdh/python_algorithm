# 연결리스트를 이용한 스택 ADT 구현

class Node:
    def __init__(self, item, next):
        self.item = item  # 노드의 값
        self.next = next  # 노드의 포인터(다음 노드를 가리킨다.)
'''
self.변수는 전역 변수처럼 사용 가능?
self.last 는 push(item) 의 경우 새로 추가된 노드를 참조한다. 
새로 추가된 노드.next 는 먼저 추가된 노드를 참조한다. 

pop() 경우 self.last.item 으로 반환할 마지막 노드의 값을 빼낸다.
값을 리턴할 item 에 담은 후, self.last = self.last.next 로 
스택의 last 노드를 먼저 추가된 노드를 참조하게 한다. 
'''
class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()

for _ in range(3):
    print(stack.pop())