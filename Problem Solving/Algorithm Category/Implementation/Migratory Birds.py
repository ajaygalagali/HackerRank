arr_count = int(input().strip())

sight = list(map(int, input().rstrip().split()))
countt=[]

for i in range(1,6):
    countt.append(sight.count(i))

answer = countt.index(max(countt))
print(answer+1)
