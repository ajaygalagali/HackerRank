# Reverse a doubly linked list
# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

def reverse(head):
    # Write your code here
    if head is None or head.next is None:
        return head

    cur = head
    prev = None
    while cur:
        nex = cur.next
        cur.next = prev
        cur.prev = nex

        prev = cur
        cur = nex

    return prev