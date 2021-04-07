# 주어진 문자열이 펠린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
import collections
import re
from typing import Deque

input="A man, a plan, a canal: Panama"


# 1.리스트로 변환 (304ms)
def is_palindrome_1(s: str) -> bool:
    strs : list[str] = []
    for char in s:
        if char.isalnum():
            strs .append(char.lower())

    while len(strs) > 1:
        if strs .pop(0) != strs .pop():
            return False
            return True
        pass

# 2.데크 자료형을 활용 (64ms)
#리스트의 pop(0)은 O(n), 반면에 데크의 popleft()는 O(1)이기 때문에
#각각 n번 반복하게 되면 O(n^2) , O(n) 으로 차이가 커진다.
def is_palindrome_2(s:str) -> bool:
    strs : Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 3. 슬라이싱 사용(36ms)
def is_palindrome_3(s:str) -> bool:
    s=s.lower()
    s=re.sub('[^a-z0-9]','',s)
    return s==s[::-1]
print(is_palindrome_3(input))
