'''
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"
'''
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # print("실행")
        counter, seen, stack = collections.Counter(s), set(), []
        # print("counter = ", counter)
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
Solution().removeDuplicateLetters("bcabc")