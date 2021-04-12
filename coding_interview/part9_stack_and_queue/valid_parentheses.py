# 유효한 괄호

input = "()[]{}"
'''
스택의 대표적인 문제이다. 
순차적으로 괄호들을 푸시하고, closing 을 만날 때 pop을 하여 결과가 일치 한지 체크한다.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        print(not stack)
        print(stack)
        # closing 을 키로, opening 을 값으로 매핑테이블 생성
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            # char 이 테이블의 키에 없다면 ),},] stack에 char 을 append
            if char not in table:
                stack.append(char)
                print(not stack)
            elif not stack or table[char] != stack.pop():  # table[char] == table.get(char) char 을 key 로 조회
                print(stack)
                return False

        return not stack
test = Solution()
print(test.isValid(input))

