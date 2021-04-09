# 연결리스트가 팰린드롬 구조인지 판별하라

# input = [1 -> 2]

'''
팰린드롬 여부를 판별하기 위해서는 앞뒤로 모두 추출할 수 있는 자료구조가 필요하다.
일반적인 스택 자료구조는 마지막 요소만 추출하는 연산자 pop() 만 있지만,
파이썬의 리스트는 pop(i) 처럼 인덱스를 지정할 수 있다.
'''
import collections
from typing import List, Deque


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    # 164ms
    def is_palindrome_1(head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    # 리스트로도 문제를 풀었지만, 데크를 이용해 최적화 할 수 있다.
    # 동적 배열로 구성된 리스트는 맨 앞 아이템을 가져오기 위한 q.pop(0) 적합한 자료형이 아니다.
    # 맨 앞 아이템을 추출하면 모든 원소들의 시프팅이 일어난다 O(n)
    # -> 양방향 모두 O(1) 에 추출이 가능한 데크 사용 (72ms)

    def is_palindrome_2(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q : Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # 러너를 이용한 풀이 64ms
    # 데크와 성능은 비슷하지만, 다른 자료형으로의 변환 없이 연결리스트 답게 풀 수 있다.
    '''
    slow, fast 러너를 동시에 출발 시킨다. slow 는 한 칸, fast 는 두 칸씩 이동한다. 
    fast 가 끝에 다다를 때 slow 는 중간에 도착한다. 
    slow 러너는 중간까지 가는 동안 역순으로 연결리스트 rev 를 만들어간다. 
    중간에 도착한 slow 러너는 남은 구간을 이동하면서 만들어둔 rev(역순 연걸리스트) 와 값을 비교해간다.
    rev 와 나머지 구간의 값이 같다면 팰린드롬이다. 
    '''
    def is_palindrome_3(self,head: ListNode) -> bool:
        rev = None
        slow = fast = head

        # 러너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:  # fast 가 끝에 다다를 때 까지
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:  # 홀수일 때는 slow 러너가 한 칸 더 이동해야 한다. 이를 fast 가 None 이 아닌 경우로 간주한다.
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        # 팰린드롬이라면 slow 와 rev 모두 끝까지 이동하여 None 이 되었을 것이다.
        return not rev

