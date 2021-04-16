'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

zip() 함수:
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어준다.

list(zip*(strs)) 를 통해
세개의 단어의 같은 인덱스 별로 묶어준다.
(가장 길이가 짧은 데이터에 길이가 맞춰진다.)

set(i) 를 통해 중복을 제거한다.
중복을 제거한 뒤 길이가 1이라면 세개의 prefix 가 모두 일치하는 것으로 판단한다.

str 에도 += 연산자를 사용한다.
'''
from typing import List

strs = ["flower", "flow", "flight"]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs_zip = list(zip(*strs))
        #  >>> strs_zip = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]

        prefix = ""

        for i in strs_zip:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix

