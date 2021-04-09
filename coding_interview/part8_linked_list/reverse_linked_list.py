# 연결 리스트를 뒤집어라

'''
input
1->2->3->4->5->NULL

output
5->4->3->2->1->NULL
'''


class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    # 재귀
    def reverse_list(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    # 반복
    def reverse_list_2(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev