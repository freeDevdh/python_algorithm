'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]
'''
import collections
from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        print((anagrams.values()))
        print(anagrams.items())
        print(anagrams.keys())
        return list(anagrams.values())

test = Solution()
print(test.groupAnagrams(strs))