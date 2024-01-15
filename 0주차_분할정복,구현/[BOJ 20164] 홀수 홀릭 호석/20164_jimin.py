from itertools import combinations

def cnt(n_str):
    n_list = list(map(int,n_str))
    cnt = 0
    for num in n_list:
        if num % 2 != 0: cnt += 1
    return cnt

n = input()

ans_min, ans_max = 1e9,0

def process(n, count):
    global ans_min, ans_max

    if len(n)==1:
        count += cnt(n)
        ans_min = min(ans_min, count)
        ans_max = max(ans_max, count)
        return
    elif len(n)==2:
        count += cnt(n)
        process(str(int(n[0])+int(n[1])), count)
    else:
        count += cnt(n)
        split_spots = list(combinations([i for i in range(1,len(n))], 2))
        for split_spot in split_spots:
            first = int(n[:split_spot[0]])
            sec = int(n[split_spot[0]:split_spot[1]])
            third = int(n[split_spot[1]:])
            cur_n = first + sec + third
            process(str(cur_n), count)

process(n, 0)

print(ans_min, ans_max)