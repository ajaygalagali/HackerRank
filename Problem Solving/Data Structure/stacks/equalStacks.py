# incomplete

h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]

isZeroHeight = False

while sum(h1)!=sum(h2)!=sum(h3):

    # if len(h1) < 1 or len(h2) < 1 or len(h3) < 1:
    #     isZeroHeight = True
    #     break

    h1.pop(0)

    if sum(h1)==sum(h2)==sum(h3):
        break

    h2.pop(0)

    if sum(h1)==sum(h2)==sum(h3):
        break

    h3.pop(0)

    if sum(h1)==sum(h2)==sum(h3):
        break

print(h1,h2,h3)

if sum(h1)!=sum(h2)!=sum(h3):
    print("Zero")
else:
    maxHeight = max(sum(h1),sum(h2),sum(h3))
    print("MaxHeight ->",maxHeight)
