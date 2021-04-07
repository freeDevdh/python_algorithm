from typing import List

input = ["h", "e", "l", "l", "o"]


# problem
# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라

# 1.two pointer 를 이용한 스왑
def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

#2.Pythonic way
def reverseString_2(s : List[str]) -> None:
    s.reverse()

#3.슬라이싱 사용
def reverseString_3(s : List[str]) -> None:
    s[:] = s[::-1]
    #s=s[::-1] 은 공간복잡도를 O(1) 로 제한되었기 때문에 변수 할당을 처리하는데 제약이 있다.
print(reverseString(input))
