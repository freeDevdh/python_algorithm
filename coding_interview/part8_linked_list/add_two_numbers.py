# 역순으로 저장된 연결리스트의 숫자를 더하라
'''
input :
( 2->4->3 ) + ( 5->6->4 )

output :
7 -> 0 -> 8

342 + 465 = 807
'''
from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # 연결리스트 뒤집기
    def reverse_list(self,head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결리스트를 파이썬 리스트로 변환
    def to_list(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def to_reversed_linked_list(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        #  뒤집어서 파이썬 리스트로 변환
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))

        '''
        현재 리스트는 문자열이 아닌 숫자형 리스트이다. 이를 합치기 위해 문자형으로 먼저 변경한 뒤, 연산을 위해 다시 숫자형으로 변경한다.
        ''.join(s)  // 문자열 리스트를 str 로 변경
        str(e) for e in a   // a의 요소들을 str 로 변경
        ''.join( str(e) for e in a )   // str 로 변경
        int( ''.join( str(e) for e in a ) )   // 다시 int 로 변경
        '''
        result_str = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        return self.to_reversed_linked_list(str(result_str))


    # 전가산기
    def add_two_numbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산

            if l1:
                sum += l2.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫 과 나머지 계산
            '''
            divmod() 는 파이썬의 내장 함수이다.
            몫과 나머지로 구성된 튜플을 리턴한다. 
            divmod(a, b) 는
            (a // b, a % b) 와 동일한 결과 출력
            '''
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next

