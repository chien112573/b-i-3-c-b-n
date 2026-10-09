a = float(input())
b = float(input())
n = float(input())

if a + b == n:
    print("+")
elif a - b == n:
    print("-")
elif a * b == n:
    print("*")
elif b != 0 and a / b == n:
    print("/")
else:
    print("NO")
