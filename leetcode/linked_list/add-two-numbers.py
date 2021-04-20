'''
역순으로 저장된 연결 리스트의 숫자를 더하라
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

'''
첫번째 풀이
연결리스트를 뒤집는다.
뒤집은 연결리스트를 리스트로 변환한다.
리스트를 문자열로 이어붙인 후 정수로 형변환한다.
값을 계산한다.
다시 연결리스트로 변환하여 반환한다.

숫자형 리스트를 단일 값으로 변경하는 방법
a = [1, 2, 3, 4, 5]

''.join(str(e) for e in a)
->'12345'

''.join(map(str,a))
->'12345'
'''
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class Solution:
    # reverse linkedList
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # converting linkedList -> python list
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list. append(node.val)
            node = node.next
        return list

    # converting python list -> linkedList
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))

        return self.toReversedLinkedList(str(resultStr))

class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # sum of two inputs
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum +=l2.val
                l2 = l2.val

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next


        return root.next

