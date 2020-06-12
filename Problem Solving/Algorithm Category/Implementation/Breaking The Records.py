n = int(input())

score = list(map(int, input().rstrip().split()))

min = score[0]
max = score[0]
min_count = 0
max_count = 0
for i in score:
    if i < min:
        min_count+=1
        min = i

    if i > max:
        max_count+=1
        max = i

print(max_count,min_count)

