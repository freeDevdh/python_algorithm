# 원형 데크 구현
class ListNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class MyCircularDeque:
    def __init__(self,k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        '''
        왼쪽, 오른쪽 인덱스 역할을 하는 head, tail 을 정의한다.
        최대 길이 정보를 k 로 설정한다.
        현재 길이 정보를 담는 변수가 될 len 을 self.len = 0 으로 따로 정의해둔다.
        '''

    # 앞쪽에 노드를 추가하는 insertFront() 구현
    def insert_front(self, value: int) -> bool:
        if self.len == self.k:
            return False  # 꽉 찬 경우
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insert_last(self,value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def delete_front(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def delete_last(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def get_front(self) -> int:
        return self.head.right.val if self.len else -1

    def fet_rear(self) -> int:
        return self.tail.left.val if self.len else -1

    def is_empty(self) -> bool:
        return self.len == 0

    def is_full(self) -> bool:
        return self.len == self.k

    # 내부에서만 사용하는 함수의 이름은 _ 로 시작한다. (PEP 8 명명규칙)
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node


    def _add(self,node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new