#계산기 깃연습

def add(a,b):
    c= a + b
    return c

def sub(a,b):
    c = a - b
    return c

def mul(a,b):
    c= a*b
    return c

def div(a,b):
    c= a/b
    return c

num1,num2 = map(int,input().split())
add = add(num1,num2)
sub = sub(num1,num2)
mul = mul(num1, num2)
div = div(num1, num2)
print(add)
print(sub)
print(mul)
print(div)


print("Hello world!")
print("브랜치 확인용이라고요")