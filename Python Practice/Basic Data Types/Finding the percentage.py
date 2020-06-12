if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        #print(student_marks)
    query_name = input()

avgDict = {}
for k,v in student_marks.items():
    # v is the list of grades for student k
    avgDict[k] = sum(v)/ float(len(v))

#print(avgDict)

#print("-------------")

answer = format(avgDict[query_name], '.2f')
print(answer)
