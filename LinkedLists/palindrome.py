def isListPalindrome(head):
    f = s = head
    prev = None
    while f and f.next:
        f = f.next.next
        prev, prev.next, s = s, prev, s.next
    if f:
        s = s.next
    while s and prev:
        if s.value != prev.value:
            return False
        if (not s and prev) or (not prev and s):
            return False
        prev, s = prev.next, s.next
    return True
