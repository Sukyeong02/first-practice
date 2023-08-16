import math

degrees = 45
radians = degrees/360 * 2 * math.pi
print(math.sin(radians))
print(math.sqrt(2)/2)

def compute_interest(amount, rate, years):
    value = amount * (1+rate/100) ** years
    return value
s1 = compute_interest(200,7,1)
s2 = compute_interest(500,1,20)
print(s1, s2)


def swap(a,b):
    a,b=b,a
    print(a)
    print(b)

(x,y) = (123,456)
swap(x,y)
print((x,y))

print(str(10) + str(12.5))

def add_triple (x, y, z = 5):
    return x + y + z
ret = add_triple(add_triple(1,3), add_triple(1,2,0))
print(ret)

def swap(tup):
    a, b = tup
    return (b, a)

a = (1, 2, 4)
a, b, c = a
c, b, a = a, c, b
a, c = swap(swap((b, c)))

print(a + c)

def foo (a , b):
   b = a
   return a * 2

a = 3
b = 5
a = foo(a, b)
print(a * b)

