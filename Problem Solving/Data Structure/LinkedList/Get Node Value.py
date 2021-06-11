# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
def getNode(head, positionFromTail):
    # Write your code here
    res = []
    cur = head

    while cur:
        res.append(cur.data)
        cur = cur.next

    return res[-1 * (1 + positionFromTail)]