# 중복 문자 제거
'''
중복된 문자를 제외하고 사전식 순서로 나열하라

input :
"cbacdcbc"

output :
"acdb"
'''
import collections

input = "cbacdcbc"
class Solution:

    # 1.재귀
    def remove_duplicate_letters(self, s: str) -> str:
        # 집합으로 정렬
        # print(set(s))
        # print(sorted(set(s)))

        '''
        set() 은 중복을 허용하지 않는다. 중복된 데이터의 경우 자동으로 제거한다.
        sorted( set(s) ) 로 중복을 제외하고 정렬된 집합을 얻는다.
        '''
        for char in sorted(set(s)):  # sorted() 는 원본에 영향을 주지않고 모든 iterable 에 작동한다.
            suffix = s[s.index(char):]  # 정렬된 접미사를 기준으로 뒤에 있는 모든 문자를 suffix 에 할당
            print(suffix)
            print("set(s) = ", set(s))
            print("set(suffix) = ", set(suffix))
            print(set(s) == set(suffix))
            print("================================")
            # 전체 집합과 suffix 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):  # 집합간의 == 순서까지 일치해야 True
                return char + self.remove_duplicate_letters(suffix.replace(char, ''))

        return ''

    # 2. 스택
    # input = "cbacdcbc"
    def remove_duplicate_letters_2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        # --> Counter({'c': 4, 'b': 2, 'a': 1, 'd': 1})
        print(counter)
        for char in s:
            counter[char] -= 1
            # --> counter[c] = 4
            if char in seen:
                continue

            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            # print("stack=",stack)
            # print("stack[-1],",stack[-1])
            # print("counter[stack[-1]]=", counter[stack[-1]])

            # 첫 번째 while 은 stack == false 이기 때문에 뒤에 stack[-1] 이 stack 이 비어 있어도 익셉션이 발생하지 않는다.
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


test = Solution()
print(test.remove_duplicate_letters_2(input))