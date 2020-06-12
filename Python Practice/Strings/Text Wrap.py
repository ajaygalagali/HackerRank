import textwrap
def wrap(string, max_width):
    warpper = textwrap.TextWrapper(width = max_width)
    op=warpper.fill(string)


    return op
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)