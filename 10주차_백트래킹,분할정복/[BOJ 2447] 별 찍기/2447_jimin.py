n = int(input())

def star(n):
    if n == 3:
        return ['***', '* *', '***']

    lines = star(n//3)          # n//3 짜리 별을 구성하는 문자열 라인 배열
    stars = []

    for line in lines:
        stars.append(line*3)

    for line in lines:
        stars.append(line + ' '*(n//3) + line)

    for line in lines:
        stars.append(line*3)

    return stars

print('\n'.join(star(n)))