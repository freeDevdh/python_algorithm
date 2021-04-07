'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
대소문자를 구분하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
'''
import collections
from typing import List
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

'''
입력값에는 대소문자가 섞여 있으며 쉼표 등 구두점이 존재한다.
따라서 데이터 클렌징(Data Cleansing)이라 부르는 입력값에 대한 전처리 작업이 필요하다.
'''


def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split() #split() 의 default는 ' '띄어쓰기
             if word not in banned]
    #리스트 표현식
    counts = collections.Counter(words)

    return counts.most_common(1)[0][0] #Counter.common_word(1)은 가장 빈도가 높은 첫번 째 단어를 출력 [('ball',2)] 이기때문에 [0][0] 으로 출력

print(most_common_word(paragraph,banned))