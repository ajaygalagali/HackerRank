grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)


def round(a):
    a = str(a)
    if int(a) > 37 and int(a) < 100:
        if int(a[1]) > 5:
            first = str(int(a[0]) + 1)
            result = first + "0"
            if int(result) - int(a) < 3:
                print(result)
            else:
                print(a)

        elif int(a[1]) < 5:
            result = a[0] + "5"
            if int(result) - int(a) < 3:
                print(result)
            else:
                print(a)
        else:
            print(a)


    else:
        print(a)


for i in range(len(grades)):
    round(grades[i])
