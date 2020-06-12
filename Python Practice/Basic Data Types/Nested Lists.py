data=[]
result=[]


def Sort(data):
    l = len(data)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (data[j][1] > data[j + 1][1]):
                tempo = data[j]
                data[j] = data[j + 1]
                data[j + 1] = tempo
    return data



n=int(input())
for _ in range(n):
    name = input()
    score = float(input())
    data.append([name,score])

data=Sort(data)


for i in range(1,n):
    if data[i][1] > data[0][1]:
        result.append(data[i][0])
        if i == n-1:
            break
        if data[i+1][1] > data[i][1]:
            break

result.sort()

for j in result:
    print(j)
