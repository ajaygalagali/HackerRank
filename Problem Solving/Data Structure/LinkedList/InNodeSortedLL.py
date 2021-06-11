# Inserting a Node Into a Sorted Doubly Linked List
# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem


def sortedInsert(head, data):
    # Write your code here

    cur = head
    prevNode = cur

    # Insert at first
    if data < head.data:
        newNode = DoublyLinkedListNode(data)
        newNode.next = head
        head = newNode
        return head

    while cur:

        if data >= prevNode.data and data <= cur.data:
            # Insert between Prev and Cur
            newNode = DoublyLinkedListNode(data)
            newNode.next = cur
            newNode.prev = prevNode
            prevNode.next = newNode
            cur.prev = newNode
            cur.next = cur.next
            return head

        prevNode = cur
        cur = cur.next


