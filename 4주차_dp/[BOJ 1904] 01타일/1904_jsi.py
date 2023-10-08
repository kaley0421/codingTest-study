N = int(input())

a, b = 1, 1

for i in range(N - 1):
    temp = a
    a = b
    b = (temp + a) % 15746

print(b)