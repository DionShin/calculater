#계산기 깃연습

def add(a,b):
    c= a + b
    return c


num1,num2 = input().split()
sum = add(num1,num2)
print(sum)