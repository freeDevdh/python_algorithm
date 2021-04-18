'''
연결 리스트를 입력받아 페어 단위로 스왑하라.

Given a linked list, swap every two adjacent nodes and return its head.
Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    일반적으로 연결리스트는 복잡한 여러 가지 값들의 구조체로 구성되어 있기 때문에
    해당 풀이 처럼 값만 바꾸는 것은 어려운 일이다.
    하지만 해당 문제는 단일 값으로 구성된 단순한 연결리스트이기 때문에 이러한 방식이 가능하다.
    노드의 연결구조는 그대로 두고 값만 바꿔주는 풀이 방법
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

    def swapPairs_loop(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음 비교를 위해 이동
            head = head.next
            prev = prev.next.next

        return root.next

    def swapPairs_recursive(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs_recursive(p.next)
            p.next = head
            return p
        return head

