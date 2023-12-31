class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        _ten = 0

        while l1 is not None or l2 is not None or _ten != 0:
            i1 = l1.val if l1 is not None else 0
            i2 = l2.val if l2 is not None else 0

            _sum = i1 + i2 + _ten
            _ten, _rem = divmod(_sum, 10)

            newNode = ListNode(_rem)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
