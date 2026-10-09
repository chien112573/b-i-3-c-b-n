x = int(input())

if x <= 100:
    tien = x * 2000
elif x <= 200:
    tien = 100 * 2000 + (x - 100) * 3000
elif x <= 300:
    tien = 100 * 2000 + 100 * 3000 + (x - 200) * 5000
else:
    tien = 100 * 2000 + 100 * 3000 + 100 * 5000 + (x - 300) * 10000

print(tien)
