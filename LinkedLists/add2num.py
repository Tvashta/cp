class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def rev(a):
    prev = None
    s1 = 0
    while a != None:
        s1 += 1
        prev, prev.next, a = a, prev, a.next
    return prev, s1


def addTwoHugeNumbers(a, b):
    a, s1 = rev(a)
    b, s2 = rev(b)
    if s1 < s2:
        a, b = b, a
    c = 0
    head = a
    prev = None
    while b != None:
        x = (a.value+b.value+c) % 10000
        c = (a.value+b.value+c)//10000
        a.value = x
        prev = a
        a, b = a.next, b.next
    if c != 0:
        if a == None:
            prev.next = ListNode(c)
        else:
            prev = None
            while a and c != 0:
                a.value += c
                c = a.value//10000
                a.value %= 10000
                prev = a
                a = a.next
            if a == None and c != 0:
                prev.next = ListNode(c)
    head, s1 = rev(head)
    return head
