import textwrap
from collections import OrderedDict
def merge_the_tools(s, k):
    # your code goes here
    n=len(s)
    eq = n//k
    wrapped = textwrap.wrap(s,k)

    for i in range(eq):
        wrapped[i]="".join(OrderedDict.fromkeys(wrapped[i]))
        print(wrapped[i])

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)