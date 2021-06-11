# Incomplete
# Runtime error - Memory error

import itertools

s = input()
print("S",s)
vowels = ['a','e','i','o','u']

v_player = 0
c_player = 0

word_list = list()
for i in range(len(s)+1):
    for combination in itertools.combinations(s, i):
        word = ""
        for j in combination:
            word+=j
        word_list.append(word)

u_wl = list(set(word_list))
u_wl.remove("")
for k in u_wl:
    if(not k.startswith(tuple(vowels)) and k in s):
        points = 0
        for i in range(len(s)):
            if s[i:].startswith(k):
                points+=1
        c_player+=points
    elif(k.startswith(tuple(vowels)) and k in s):
        points = 0
        for i in range(len(s)):
            if s[i:].startswith(k):
                points += 1
        v_player += points


if(v_player > c_player):
        print("Kevin",v_player)
elif(v_player==c_player):
    print("Draw")
else:
    print("Stuart",c_player)