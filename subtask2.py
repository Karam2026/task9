n = 0
s = 0
x = int(input("Enter number: "))
m = x if x != -1 else -1

while x != -1:
    s += x
    n += 1
    if x < m:
        m = x
    x = int(input("Enter number: "))

a = -1 if n == 0 else s / n
print(n, s, m, a)

