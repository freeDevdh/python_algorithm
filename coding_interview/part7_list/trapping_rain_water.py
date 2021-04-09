# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
from typing import List

input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


# 1.투 포인터 활용
def trap(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    print("left, right =", 0, len(height)-1)
    left_max, right_max = height[left], height[right]
    print("left_max, right_max = ", height[left], height[right])
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        print("left_max = ", max(height[left], left_max))
        print("right_max = ", max(height[right], right_max))

        if left_max <= right_max:
            print("--------if문-------")
            volume += left_max - height[left]
            print("left_max =", left_max)
            print("left = ", left)
            print("height[left] = ", height[left])
            print("volume = ", volume)
            left += 1
            print("----------if문 종료")
        else:
            print("---------else문----------")
            volume += right_max - height[right]
            right -= 1
            print("---------else문 종료--------")

    return volume


#2.스택 이용
def trap_2(height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):

        #stack[-1] 은 top을 제거하지않고 반환한다.
        while stack and height[i] > height[stack[-1]]:

            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume

print(trap_2(input))
