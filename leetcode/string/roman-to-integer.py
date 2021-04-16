'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900
IV : 4
IX : 9
XL : 40
XC : 90
CD : 400
CM : 900

Input: s = "MCMXCIV"
Output: 1994

Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

주어진 로마 숫자를 아라비아 숫자로 컨버팅하라

map() 함수 :
여러 개의 데이터를 한 번에 다른 형태로 변환할 때 사용하는 파이썬 내장함수
여러 개의 데이터를 담고 있는 list 나 tuple 을 대상으로 주로 사용한다.

'''

s = "III"
class Solution:
    def romanToInt(self, s: str) -> int:
        table ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s.replace("IV", "IIII")\
            .replace("IX", "VIIII")\
            .replace("XL", "XXXX")\
            .replace("XC", "LXXXX")\
            .replace("CD", "CCCC")\
            .replace("CM", "DCCCC")

        number = 0
        for char in s:
            number += table[char]

        return sum(map(table.get, s))




