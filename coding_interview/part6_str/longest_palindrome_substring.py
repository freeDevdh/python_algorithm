'''
가장 긴 팰린드롬 부분 문자열을 출력하라

투 포인터를 사용하여 (짝수, 홀수)
팰린드롬일 경우 양 쪽으로 확장하여 가장 긴 팰린드롬을 찾는다.
'''

input = "babad"
input2 = "cbbd"


def longest_palindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # left와 right 가 범위 내에 위치하고, 양 쪽 문자가 일치하는 경우 반복
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result
'''
해당 문제에서는 
0-1 / 1-2 / 2-3 처럼 expand(i, i + 1) 에 만족하는 경우는 없다. (짝수 포인터)
0-2 / 1-3 /2-5 expand(i, i + 2) 가 만족한다. (홀수 포인터)

expand() 함수 내부에서는 left 는 좌측으로, right 는 우측으로 확장해 가면서 팰린드롬의 여부를 확인한다.
가장 긴 팰린드롬 서브 스트링을 리턴한다 . return [left + 1:right] 
-->가장 긴 팰린드롬은 결국 가장 작은 left 인덱스 값과 가장 큰 right 인덱스 값을 찾아 그 사이에 해당하는 서브스트링을 찾는 것
'''
print(longest_palindrome(input))