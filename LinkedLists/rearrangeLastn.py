# Given a singly linked list of integers l and a non-negative integer n,
# move the last n list nodes to the beginning of the linked list.
# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

# My naive implementation


def rearrangeLastN(l, n):
    head = cur = l
    size = 0
    tail = cur
    while cur != None:
        tail = cur
        cur = cur.next
        size += 1
    if n >= size or n == 0:
        return l
    size -= n
    cur = l
    while cur != None and size > 1:
        cur = cur.next
        size -= 1
    l = cur.next
    cur.next = None
    tail.next = head
    return l

# Better code


def rearr(l, n):
    fast = slow = l
    for _ in range(n):
        if not fast:
            return l
        fast = fast.next
    if not fast:
        return l
    # Fast and slow are n steps away! Move this window to the last
    while fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = l
    l, slow.next = slow.next, None
    return l
