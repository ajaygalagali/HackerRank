nkq = input().split()

n = int(nkq[0])

k = int(nkq[1])

q = int(nkq[2])

a = list(map(int, input().rstrip().split()))

queries = []

for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)

for i in range(k):
    pop = a.pop()
    a.insert(0, pop)

for i in queries:
    print(a[i])

