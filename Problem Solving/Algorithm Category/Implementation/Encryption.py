s = input()
import math
import textwrap

p = s.replace(" ", "")

l = len(p)
sq = math.sqrt(l)
c = math.ceil(sq)
f = math.floor(sq)

w = textwrap.fill(s, c)

arr = w.split()

for i in range(c):
    for j in range(c):
        try:
            print(arr[j][i], end="")

        except IndexError:
            pass
    print(" ", end="")



