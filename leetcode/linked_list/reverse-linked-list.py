'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next



class Solution:
    head = [1, 2, 3, 4, 5]

    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    def reverseList_2(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    def reverseList_3(self, head: ListNode) -> ListNode:
        prev = None
        next = None
        curr = head
        '''
        prev 는 이전의 값을 저장
        next 는 curr.next 값을 임시로 보존
        curr 은 현재 노드의 위치
        curr = head 로 초기화 시 curr 은 1 이다.
        
        1. 현위치.next 를 임시로 저장한다.,
        2. 현위치->prev 연결시킨다
        3. prev 에 노드를 저장한다.
        4. 현위치 <-> next 바꾼다.
        '''
        while(curr):  # while current not null
            next = curr.next  # saving the next
            curr.next = prev  # reversing the pointer
            prev = curr  # pre to curr
            curr = next

        return prev



