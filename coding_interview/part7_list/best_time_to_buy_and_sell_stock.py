# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라

# 1. 브루트 포스 O(n^2) (timeout)
import sys
from typing import List

input = [7, 1, 5, 3, 6, 4]

def max_profit(prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

# 2. 저점과 현재 값과의 차이 계산 O(n) (64ms)
'''
포인터가 우측으로 이동하면서 이전 상태의 저점을 기준으로 가격 차이를 계산하고, 
만약 클 경우 최댓값을 계속 교체해가는 형태로 O(n) 풀이가 가능하다.
'''
def max_profit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize  # 언제나 교체 될 수 있도록 최소값을 최대값으로 셋팅해논다.

    # 최소값과 최대값을 계속 갱신한다.
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit