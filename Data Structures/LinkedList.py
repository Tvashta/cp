class Node:
    def __init__(self):
        self.val = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # def printL(self):
    #     cur = self.head
    #     while cur != None:
    #         print(cur.val)
    #         cur = cur.next
    #     print()

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur != None:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = Node()
            self.head.val = val
        else:
            cur = Node()
            cur.val = val
            cur.next = self.head
            self.head = cur
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur1 = Node()
        cur1.val = val
        cur.next = cur1
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size+1:
            self.addAtTail(val)
            return
        if index > self.size+1:
            return
        cur = self.head
        while cur != None:
            if i == index-1:
                break
            cur = cur.next
            i += 1
        if i == index-1:
            cur1 = Node()
            cur1.val = val
            cur1.next = cur.next
            cur.next = cur1
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        if index >= self.size:
            return
        cur = self.head
        while cur.next != None:
            if i == index-1:
                cur.next = cur.next.next

                return
            cur = cur.next
            i += 1

        """
        Delete the index-th node in the linked list, if the index is valid.
        """


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
