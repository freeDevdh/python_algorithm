# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
from typing import List

nums = [-1, 0, 1, 2, -1, -4]


# 1.브루트포스로 계산 (timeout)

# 같은 값이 있는 경우 정렬을 먼저 수행하여 편하게 계산

def three_sum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()  # 정렬

    for i in range(len(nums) - 2):

        # 중복된 값 건너뛰기
        # 해당 문제는 합이 0 인 세개의 엘리먼트를 찾는 것이므로
        # 중복된 값은 또 연산할 필요가 없다.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
    return results

# 투 포인터로 계산
def three_sum_2(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 간격을 좁혀가며 sum 계산
        # left 와 right 의 초기값은 i+1 과 리스트의 마지막
        left, right = i + 1, len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] +nums[right]
            # nums.sort()로 이미 오름차순으로 정렬되어 있다.
            # 앞에 있을수록 낮은 수 이기 때문에 sum < 0 인 경우 left 를 한 칸 뒤로 민다.
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else : # sum == 0 인 경우
                # results 에 추가한다.
                results.append([nums[i], nums[left], nums[right]])

                # left 와 right 옆에 있을 수 있는 동일한 값을 넘어간다.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 또 답을 찾기 위해 하나씩 증가 시켜 반복문으로 다시 검색한다.
                left += 1
                right -= 1

    return results



print(three_sum_2(nums))
