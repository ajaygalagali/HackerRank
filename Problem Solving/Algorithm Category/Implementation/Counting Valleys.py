n = int(input())

s = input()

result = 0
p_res = 0
valley = 0

for i in range(len(s)):

    if s[i] == "U":
        step = 1
    else:
        step = -1

    result += step

    if i != 0:
        if s[i - 1] == "U":
            step2 = 1
        else:
            step2 = -1
        p_res += step2

    if p_res < 0 and result >= 0:
        valley += 1

print(valley)

