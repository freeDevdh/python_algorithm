# 정렬되어 있는 두 연결 리스트를 합쳐라
'''
input :
1->2->4, 1->3->4

output:
1->1->2->3->4->4
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1  # 다중할당을 이용한 파이썬만의 스왑
        if l1:
            l1.next = self.merge_two_lists(l1.next, l2)
        return l1