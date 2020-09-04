
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def mergeTwoLinkedLists(l1, l2):
    cur = head = None
    while l1 != None and l2 != None:
        if l1.value < l2.value:
            if head:
                head.next = l1
                head = head.next
            else:
                head = l1
                cur = head
            l1 = l1.next
        else:
            if head:
                head.next = l2
                head = head.next
            else:
                head = l2
                cur = head
            l2 = l2.next
    while l1 != None:
        if not head:
            head = l1
            if not cur:
                cur = head
        else:
            head.next = l1
            head = head.next
        l1 = l1.next
    while l2 != None:
        if not head:
            head = l2
            if not cur:
                cur = head
        else:
            head.next = l2
            head = head.next
        l2 = l2.next
    return cur
