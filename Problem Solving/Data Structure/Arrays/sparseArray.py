strings = ['aba','baba','aba','xzxb']
query = ['aba','xzxb','ab']


lenStrings = len(strings)
lenQuery = len(query)


res = []



for q in query:
    count = 0
    for s in strings:

        if q == s:
            count+=1
    res.append(count)

print(res)
