N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

numbers.sort()

def bin_search(numbers, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if numbers[mid] == target:
      print(1)
      return
    elif numbers[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  print(0)

for target in targets:
  bin_search(numbers, target, 0, N - 1)
