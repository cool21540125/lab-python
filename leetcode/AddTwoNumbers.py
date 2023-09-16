class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.__class__.__name__}{{val: {self.val}, next: {self.next}}}"

    def __eq__(self, other):
        try:
            if self.val == other.val:
                next_self = self.next
                next_other = other.next
                while next_self:
                    if next_self.val != next_other.val:
                        return False
                    next_self = next_self.next
                    next_other = next_other.next
                return True
            else:
                return False
        except Exception:
            return False


class LinkedList:
    listnode = None

    def __init__(self, list_data):
        for data in reversed(list_data):
            self.insert_at_begin(data)

    def insert_at_begin(self, data):
        new_node = ListNode(data)
        if self.listnode is None:
            self.listnode = new_node
        else:
            new_node.next = self.listnode
            self.listnode = new_node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            list1 += str(l1.val)

        list2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            list2 += str(l2.val)

        mm = max(len(list1), len(list2))

        _ten = _rem = 0
        _combined = ""
        for idx in range(mm):
            i1 = int(list1[idx]) if idx < len(list1) else 0
            i2 = int(list2[idx]) if idx < len(list2) else 0
            _sum = i1 + i2 + _ten
            _ten, _rem = divmod(_sum, 10)
            _combined += str(_rem)

        if _ten > 0:
            _combined += str(_ten)

        return LinkedList(list(map(int, _combined))).listnode
