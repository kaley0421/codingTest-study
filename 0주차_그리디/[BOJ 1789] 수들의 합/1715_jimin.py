s = int(input())

answer = 0
num = 1

while s >= num:
    s -= num
    num += 1
    answer += 1

print(answer)