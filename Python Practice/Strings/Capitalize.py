


# Complete the solve function below.
def solve(s):
    li = s.split(" ")
    string=""

    for i in range(len(li)):
        string = string + li[i].capitalize() + " "
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()