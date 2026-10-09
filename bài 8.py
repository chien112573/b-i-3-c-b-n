a = float( input())
b = float( input())
c = float( input())
if a == b == c:
    print ("Tam giác đều ")
elif a == b or b == c or c == a:
    print("tam giác cân")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("tam giác vuông")
else:
    print("tam giác thường")
