def reverseNodesInKGroups(l, k):
    h = jump = ListNode(0)
    h.next = left = right = l
    while True:
          i = 0
           while i < k and right:
                i += 1
                right = right.next
            if i == k:
                prev = right
                cur = left
                for _ in range(k):
                    cur.next, cur, prev = prev, cur.next, cur
                jump.next, jump, left = prev,left,right
            else:
                return h.next
