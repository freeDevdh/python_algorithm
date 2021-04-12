# 파이썬

## 기초
### 사칙연산
a // b : 몫 (소수점 이하는 버린다.)
a % b : 나머지
divmod(a,b) : (a // b, a % b) 와 같다.
a**b : a의 b승 (거듭제곱)
int( a ) : int 로 형변환 (문자열 정수도 가능)

2진수 : 0b110 -> 6
8진수 : 0o10 -> 8
16진수 : 0xF -> 15

### 실수
float(숫자)
float(1 + 2)
float( '5.3' )

### 변수
**명명규칙**
영문 문자와 숫자를 사용할 수 있다.
대소문자를 구분한다.
문자부터 시작해야하며 숫자로 시작할 수 없다.
언더바(_) 로 시작할 수 있다.
특수문자는 사용할 수 없다.
키워드는 사용할 수 없다.

파이썬은 **다중할당**이 가능하다.
-> x, y, z = 10, 20, 30

파이썬의 None 은 자바의 Null

파이썬은 모든 것이 객체다. 기본형이 없다.

불변객체(immutable) :
bool / int / float / tuple / str

가변객체(mutable) :
list / set / dict 

### 입력
user = input(str)
정수로 형변환
user = int( input(str) ) 

다중 입력
a, b = input(str).split() // default 는 공백

map 을 사용하여 정수로 변환 입력
a, b = map(int, input(str).split() )

### 출력
sep 으로 값 사이에 문자를 넣어 출력
print(1, 2, 3, sep = ',')
-> 1, 2, 3
print(1920, 1080, sep = 'x')
-> 1920x1080

**공백 출력**
print(1, 2, 3, sep='\n') or
print('1\n2\n3\n') 
->
1
2
3

### 비교
== 는 값을 비교한다.
is 는 객체(참조값)를 비교한다. 

### 리스트
여러가지 자료형을 섞어서 저장 가능하다.
**리스트 생성**
빈 리스트

리스트 = []
리스트 = list()

range() 사용
리스트 = list( range(start, end, gap) )

### 튜플
튜플은 리스트와 비슷하지만, 데이터를 변경, 추가, 삭제 할 수 없다.
(읽기 전용 리스트)

**튜플 생성**
( ) 괄호로 묶어준다.
a = (1, 2, 3) 

튜플도 리스트 처럼 여러 자료형을 섞어서 저장 가능하다. 

요소가 한 개인 튜플 생성
(1,)

range() 사용

튜플 = tuple( range(start, end ,gap) )

### 튜플 <-> 리스트
a = [1, ,2, 3]  // 리스트
tuple( a )
-> (1, 2, 3)

b = (4, 5, 6)  //튜플
list( b )
->[4, 5, 6]

**리스트와 튜플로 변수 만들기**
a, b, c = [1, 2, 3]
-> a=1, b=2, c=3
a, b, c = (1, 2, 3)
-> a=1, b=2, c=3
변수의 개수와 요소의 개수는 같아야 한다.

### 시퀀스 자료형
값이 연속적으로 이어져 있는 자료형
list / tuple / range / str / bytes / bytearray

**특정 값이 있는지 확인하기**
a = [1, 2, 3, 4]
1 in a
-->True
5 in a
-->False
**시퀀스 객체 연결하기**
a= [1, 2, 3], b= [4, 5, 6]
a + b
-->[1, 2, 3, 4, 5, 6]
**range 는 + 연산자로 연결 불가**
**리스트와 튜플의 요소 개수 구하기**
a = [1, 2, 3, 4]
len(a)
-->4

### 딕셔너리
딕셔너리 = { 키1: 값1, 키2: 값2}
딕셔너리 = {}
딕셔너리 = dict()
**딕셔너리에 저장할 때 키가 중복되면 가
장 뒤에 있는 값만 사용한다.**
**키에는 리스트와 딕셔너리를 제외하고 모든 자료형을 사용할 수 있다.**
**딕셔너리에 키가 있는지 확인하기**
key in dict
-->bool
**딕셔너리의 키 개수 구하기**
len(dict)
-->int

### 리스트와 튜플 응용하기
append : 요소 하나를 추가
extend : 리스트를 연결하여 확장
insert : 특정 인덱스에 요소 추가

**리스트의 할당과 복사**
a=[1, 2, 3, 4]
b = a
a is b 
-->True
b[0] = 100
a
-->[100, 2, 3, 4]
b
-->[100, 2, 3, 4]
리스트 a 와  b를 완전히 두 개로 만들기 위해서는 copy 메서드 사용
a = [1, 2, 3, 4]
b = a.copy()
a is b 
-->False
a == b
True

**리스트 컴프리헨션**
파이썬의 리스트가 특이한 점은 리스트 안에 for, if 를 사용할 수 있다는 점이다.
이렇게 리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 생성하는 것을 리스트 컴프리헨션이라고 한다.

a= list(i for i in range(10) ) or
a= [ (i for i in range(10) ]
a
-->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a=list( i for in range(10) if i % 2 == 0) or
a = [i for i in range(10) if i % 2 == 0]
a
-->[0, 2, 4, 6, 8]

**리스트에 맵 사용하기**
map 은 리스트의 요소를 지정된 함수로 처리해주는 함수이다.(map 은 원본 리스트를 변경하지 않고 새 리스트를 생성한다.)

**실수가 저장된 리스트의 요소를 정수로 바꾸기**
a = [1.2, 2.5, 3.7]
for i in range( len(a) ):
	a[i] = int(a[i[])
a
-->[1, 2, 3, 4]

map 사용
a = list(map(int,a))
a
-->[1, 2, 3, 4]

**튜플의 메서드**
튜플은 리스트와 달리 내용을 변경할 수 없다. (불변객체)
따라서 내용을 변경하는 append 같은 메서드는 사용할 수 없고, 요소의 정보를 구하는 메서드만 사용할 수 있다.

**튜플에서 특정 값의 인덱스 구하기**
a.index(값)
-->index
**특정 값의 개수 구하기**
a.count(값)
-->값의 개수

### 문자열 응용하기
str.replace('old', 'new)

table = str.maketrans('abc','123')
'apple'.translate(table)
-->1pple

str.split() //default 공백

' ' join(['apple', 'banana', 'melon'])
-->apple banana melon
'-'.join(['apple', 'banana', 'melon'])
-->apple-banana-melon

str.upper()
str.lower()

str.rstrip()
str.lstrip()
str.strip()
str.rstrip('삭제할문자열')
str.lstrip('삭제할문자열')
str.strip('삭제할문자열')

str.ljust(문자열길이)
str.rjust(문자열길이)
str.center(문자열길이)

str.zfill(길이)
길이만큼 문자열을 생성한 뒤 앞에서 부터 0을 채운다.

str.find('찾을문자')
-->index or -1
str.rfind('찾을문자') //오른쪽부터 찾는다.
-->index or -1

str.index('찾을문자')
str.rindex('찾을문자')
-->index or error

str.count('문자열')
-->문자열 등장 개수

**구두점 삭제 팁**
import string
string.punctuation
-->'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
