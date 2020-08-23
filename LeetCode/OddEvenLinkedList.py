# Definition for singly-linked list.
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# This is done for values
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = None
        even = None
        oddst = None
        evenst = None
        isOdd = True
        while head != None:
            if odd == None and isOdd:
                odd = copy.copy(head)
                oddst = odd
            elif even == None and not isOdd:
                even = copy.copy(head)
                evenst = even
            else:
                if isOdd:
                    odd.next = copy.copy(head)
                    odd = odd.next
                else:
                    even.next = copy.copy(head)
                    even = even.next
            isOdd = not isOdd
            head = head.next

        even.next = None
        odd.next = evenst
        return oddst
