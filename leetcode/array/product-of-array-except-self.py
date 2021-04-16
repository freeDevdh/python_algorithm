'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

나눗셈을 하지 않고 O(n)에 풀이하라
->미리 전체 곱셈 값을 구해놓고 각 항목별로 자기 자신을 나눠서 풀이하는 방법은 안 된다는 뜻이다.
'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1,0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out