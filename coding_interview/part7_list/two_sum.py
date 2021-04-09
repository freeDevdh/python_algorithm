# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
from typing import *

nums = [2, 7, 11, 15]
target = 9


# 1.브루트포스 방식 , 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인 (5284ms)
def two_sum_1(nums : List[int], target : int) -> List[int]:
    for i in range(len(nums)):
        for j in range((i+1),len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# 2.in을 이용한 탐색 (864ms)
# 모든 조합을 비교하지 않고, 타겟에서 첫 번째 값을 뺀 target-n이 존재하는지 탐색하는 문제로 변경
def two_sum_2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n
        '''
        enumerate()
        반복문에서 인덱스와 원소에 대한 동시 접근을 위해 사용한다.
        위의 반복문에서 i는 인덱스, n은 원소를 의미한다.
        enumerate() 함수는 인자를 가지고 튜플을 생성해준다.
        enumerate(nums,start=1) 방식으로 시작 인덱스를 지정할 수도 있다. 
        '''

        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

# 3.첫 번째 수를 뺀 결과 키 조회 (48ms)
'''
타겟에서 첫 번째 수를 빼면 두 번째 수를 바로 알아낼 수 있다. 
그렇다면 두 번째 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리로 저장한다면, 
두 번째 수를 키로 조회해서 정답을 찾을 수 있다. 
타겟에서 첫 번째 수를 뺀 결과를 키로 조회하여 두 번째 수의 인덱스를 찾는다. 
'''
def two_sum_3(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    #키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
        print(num ,nums_map[num])

    #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            print("i = ", i)
            print("num = ", num)
            print("target - num = ", (target - num))
            print("nums-map[target - num] = ", nums_map[target - num])
            return [i, nums_map[target - num]]


#4. 3번을 하나의 for문으로 통합
def two_sum_4(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map: #첫 번째 숫자는 건너뛴다.
            return [nums_map[target - num],i]
        nums_map[num] = i #키와 값을 뒤집어 저장 

print(two_sum_4(nums, target))

