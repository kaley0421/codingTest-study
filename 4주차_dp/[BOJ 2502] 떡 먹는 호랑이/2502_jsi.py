D, K = map(int, input().split())

cur = K // 2 + 1
prev = K - cur

idx = 0
date = D - 1
num = K

while 2 < date:
    num = cur
    cur = prev
    prev = num - cur
    date -= 1
    
    if prev < 0 or cur < prev:
        date = D - 1
        idx += 1
        cur = K // 2 + 1 + idx
        prev = K - cur

print(prev)
print(cur)