# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. (인덱스 기준)
# 공간복잡도 O(1), 시간복잡도 O(n) 에 풀이하라.

'''
input :
1->2->3->4->5->NULL

output :
1->3->5->2->4->NULL

홀, 짝 각 노드를 구성한 다음 홀수 노드의 마지막을 짝수 노드의 처음과 이어준다.
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next
class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head


