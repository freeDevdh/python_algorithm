# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
from typing import List

input = [1, 4, 3, 2]
'''
n은 2가 되며, 최대 합은 4이다.
min(1,2) + min(3,4) = 4

페어의 min()을 합산했을 때 최대를 만드는 것은 결국 min() 이 커야 한다는 것이다.
오름차순으로 정렬한 뒤 순서대로 min(a,b)를 하면 최대 값이 된다. 
내림차순으로 정렬한 뒤 뒤에서 부터 하여도 결과는 같다. 
'''


# 1. 오름차순 정렬 후 풀이
def array_pair_sum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()  # 오름차순 정렬

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []  # 페어를 비워준다.

    return sum


# 2. 짝수 번째 값 계산
# 정렬된 상태에서는 항상 짝수 번째에 작은 값이 위치한다.
def array_pair_sum_2(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum


# 3. Pythonic way
def array_pair_sum_3(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
'''
sort() 와 sorted() 

sorted() 
새로운 정렬된 목록을 반환하며, 기존의 목록은 영향받지 않는다.
리스트 뿐만 아니라 문자열, 튜플, 딕셔너리, 제너레이터 등 반복 가능한 객체에 모두 사용가능하다.

sort()
리스트에만 사용가능하다. 
기존 목록을 정렬하며, None 을 반환한다. 
리스트의 경우 list.sort() 는 복사본을 만들 필요가 없으므로 sorted() 보다 빠르다. 
    


'''

print(array_pair_sum_3(input))
