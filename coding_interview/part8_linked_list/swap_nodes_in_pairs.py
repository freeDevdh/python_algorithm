# 연결 리스트를 입력받아 페어 단위로 스왑하라
'''
input :
1->2->3->4

output :
2->1->4->3
'''

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    # 1.값만 교환 (빨리 풀기 위한 방법 중 하나) 풀이 2,3번에 대한 이해가 숙지되어야 한다.
    def swap_pairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            #값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head

    # 2. 반복 구조로 스왑
    def swap_pairs_2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # b가 a(haed) 를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            #다음 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        '''
        연결 리스트의 head 를 가리키는 노드가 직접 바뀌는 풀이이므로
        head 를 리턴하지 못하고 그 이전 값을 root로 별도 설정한 다음 root.next 를 리턴
        '''
        return root.next

    # 3. 재귀 구조로 스왑
    def swap_pairs_3(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            #스왑된 값 리턴 받음
            head.next = self.swap_pairs_3(p.next)
            p.next = head
            return p

        return head