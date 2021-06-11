# Delete duplicate-value nodes from a sorted linked list
# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

def removeDuplicates(head):
    # Write your code here
    cur = head
    prevNode = None
    prevValue = None

    while cur:
        curValue = cur.data
        if prevValue == curValue:
            prevNode.next = cur.next
        else:
            prevValue = curValue
            prevNode = cur

        cur = cur.next

    return head
