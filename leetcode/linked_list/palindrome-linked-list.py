'''
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
'''


# Definition for singly-linked list.
import collections
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

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

    def isPalindrome_2(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head  # 느린 러너와 빠른 러너를 동일한 시작점에서 시작한다.

        while fast and fast.next:
            fast = fast.next.next  # 빠른 러너는 두 칸씩
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev



