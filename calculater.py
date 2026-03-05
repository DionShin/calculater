#계산기 깃연습

def add(a,b):
    c= a + b
    return c

def sub(a,b):
    c = a - b
    return c


num1,num2 = map(int,input().split())
add = add(num1,num2)
sub = sub(num1,num2)
print(add)
print(sub)