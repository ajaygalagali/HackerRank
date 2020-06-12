def split_and_join(line):
    # write your code here
    op=line.split(" ")
    op="-".join(op)
    return op
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)