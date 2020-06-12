
string = str(input())
for i in string:
    if i.isalnum():
        print("True")
        break
else:
    print("False")

for i in string:
    if i.isalpha():
        print("True")
        break
else:
    print("False")

for i in string:
    if i.isdigit():
        print("True")
        break
else:
    print("False")

for i in string:
    if i.islower():
        print("True")
        break
else:
    print("False")

for i in string:
    if i.isupper():
        print("True")
        break
else:
    print("False")
