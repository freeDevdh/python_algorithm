# 매일의 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력하라
'''
T = [73, 74, 75, 71, 69, 72, 76, 73]

output :
[1, 1, 4, 2, 1, 1, 0, 0]
현재의 인덱스를 계속 스택에 쌓아두다가, 이전보다 상승하는 지점에서 현재 온도와 스택에 쌓아둔 인덱스 지점의
온도 차이를 비교해서, 더 높다면 다음과 같이 스택의 값을 팝으로 꺼내고 현재 인덱스와 스택에 쌓아둔 인덱스의 차이를
정답으로 처리한다.
'''
from typing import *


class Solution:
    T = [73, 74, 75, 71, 69, 72, 76, 73]

    def daily_temperature(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        print("answer = ", answer)
        stack = []
        loop = 1
        print("-----------------")
        for i, cur in enumerate(T):
            print(i, "번 째 for 반복")
            loop += 1
            loop2 = 1
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > T[stack[-1]]:
                print(loop2, "번 째 while 반복")
                loop += 1

                print("stack =", stack)
                print("stack[-1] = ", stack[-1])
                print("T[stack[-1]] = ", T[stack[-1]])

                last = stack.pop()
                print("last = ", last)
                print("i - last = ", (i-last))
                answer[last] = i - last
            stack.append(i)

        return answer
test = Solution()
print(test.daily_temperature(test.T))