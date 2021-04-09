# 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
'''
input :
1->2->3->4->5->NULL , m=2, n=4

output :
1->4->3->2->5->NULL
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:

        print(m)
        print(n)

        # 예외 처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        # start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

    def print_list(list: ListNode):
        for i in list:
            print(i)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

a = Solution()

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6



print(a.print_list(a.reverse_between(node1, 4, 2)))

