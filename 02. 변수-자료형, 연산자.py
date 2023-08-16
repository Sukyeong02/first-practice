a = 1
b = 2
print(a+b)

c = True
print(c)
print(type(c))

i = 15
print(i)
print(type(i))

f = 12.34
print(f)
print(type(f))

l = [1,'bts',3]
print(l)
print(type(l))

t = (1,2,3)
print(t)
print(type(t))

r = range(10)
print(r)
print(type(r))

d = {1:'one', 2:'two'}
print(d)
print(type(d))

#bool 은 0이나 False가 아니면 모두 true로 변환
print(bool(True))
print(bool(False))
print(bool(10))
print(bool(0b010))

#int / 불리언 값은 True는 1로, False는 0으로 변환
print(int(True))
print(int(False))
print(int(10))
print(int(0b010)) #2진수

#float형은 자료형을 실수형으로 변환 / int와 유사하지만 소수점 이하 값이 포함
print(float(True))
print(float(False))
print(float(10))
print(float(0b010))

#str형은 문자열로 변환 / repr() 도 존재 / str()는 내부적으로 __str__ 메소드 호출(객체의 비공식적인 문자열 출력에 사용되며 
# 사용자가 보기 좋은 쉬운 형태로 보여줄 때 사용 / repr은 공식적인 문자열을 출력할 때 사용되며, 주로 해당 객체를 인식할 수 있는 
# 공식적인 문자열 나타낼 때 사용)
print(str(True))
print(str(False))
print(str(10))
print(str(0b010))

#tuple
print(tuple('susan'))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#list
print(list('susan'))
print(list([1,2,3]))
print(list((1,2,3)))

#set 집합형 : 요소에 대한 순서 고려 없음, 딕셔너리의 경우 키 값에 해당하는 것만 집합으로 변환

#자료형 계산
# min, max, sum, divmod(a,b):a를 b로 나눈 값과 나머지를 쌍으로 반환, abs(x):절댓값 반환, pow(a,b):a의 b승을 반환
# len(s):길이, round(x):소수점 뒤를 반올림한 값 반환, all():모든 값이 True이거나 비었을 때 True반환, any():어떤 값이 True이면 True 반환
# 값이 비어있을 때 False반환
print(min(1,2,3))
print(max(4,8,15))
print(sum((1,5,8)))
print(divmod(4,18))
print(abs(-10))
print(pow(4,2))
print(len('America'))
print(round(3.141592, 2))
print(all((1,2,3)))
print(all((False, True, False)))
print(any((1,2,3)))
print(any((False, True, False)))

#연산자:산술, 비교, 할당(=,+=,-= 등등), 비트(& and, | or, ^ xor, ~ not), 논리(and, or, not), 멤버(in, not in), 식별(is, is not)

#연산자 우선순위 : 괄호 -> 논리연산자

if 3>4:
    print('3이 4보다 큽니다.')
else:
    print('3이 4보다 크지 않습니다.')

a = 5
if 3>4:
    a=3
    a+=3
print(a)

if not True :
    print("A")
elif True != True :
    print("B")
elif (not True) != False :
    print("C")
elif False == (not True) :
    print("D")
else :
    print("E")

a = 4
while a != 10:
    a += 2
print(a)

tup = (10,20,30,40)
a,b,c,d = tup
a,b,c,d = b,c,d,a
print(a + c)

def compute():
    return 3 * 4 / 2
a = 8 * compute() / 2 * 4
print(a)

 

sum = 0
for x in range(3):
    for y in range(2):
     sum = sum + y
print(sum)