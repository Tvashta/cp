# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    c = l
    while l != None and l.next != None:
        if l.next.value == k:
            l.next = l.next.next
        else:
            l = l.next
    while c != None and c.value == k:
        c = c.next
    return c
