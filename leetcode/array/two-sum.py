'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            ans = target - n

            if ans in nums[i + 1:]:
                return [i, nums[i + 1:].index(ans) + (i + 1)]
    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, n in enumerate(nums):
            nums_map[n] = i

        for i, n in enumerate(nums):
            if target - n in nums_map and i != nums_map[target - n]:
                return [i, nums_map[target - n]]
    def twoSum_4(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target - n], i]
            nums_map[n] = i


nums = [2, 7, 11, 15]
target = 9
test = Solution()
print(test.twoSum_2(nums, target))