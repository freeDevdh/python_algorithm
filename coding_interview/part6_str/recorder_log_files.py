# 로그를 재정렬하라
# 1.로그의 가장 앞 부분은 식별자다
# 2.문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3.식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
# 4.숫자 로그는 입력 순서대로 한다.
from typing import List

logs = ["digi1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


# key
# 문자와 숫자를 구분한다. 그 뒤 숫자를 나중에 이어 붙인다.

def recorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []  # letters 는 문자 배열, digits 는 숫자 배열
    for log in logs:
        print(log.split()[1])
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
#람다식
'''
def func(x):
    return x.split()[1], x.split()[0]
s.sort(key=func)

이를 람다식으로 표현하면

s.sort(key= lanbda x: (x.split()[1], x.split()[0]))
'''
print(recorderLogFiles(logs))
