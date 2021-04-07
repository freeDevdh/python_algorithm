'''
문자열 배열을 입력 받아 애너그램 단위로 그룹핑하라

'애너그램'이란?
->문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.
'문전박대' -> '대박전문'

'''
import collections
from typing import List

input = ["eat", "tea", "ate", "nat", "bat"]

def group_anagrams(strs : List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
        #''.join(str) 은 str을 공백에 이어붙인다.
        #sorted(str) 은 문자열을 정렬하여 리스트 형태로 반환

    return list(anagrams.values())

print(group_anagrams(input))

