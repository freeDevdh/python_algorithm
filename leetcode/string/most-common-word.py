'''
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
'''
import collections
from typing import List
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # words = [word for word in re.sub(r'[^\w]', '', paragraph)
        #     .lower().split()
        #          if word not in banned]
        words =[word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split()
                    if word not in banned]
        print(words)
        counter = collections.Counter(words)
        print(counter)
        return counter.most_common(1)[0][0]

test = Solution()
print(test.mostCommonWord(paragraph, banned))
