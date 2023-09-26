from leetcode.AddTwoNumbers import Solution as AddTwoNumbers, ListNode
import pytest


class TestAddTwoNumbers:
    @pytest.mark.parametrize(
        "list1, list2, target",
        [
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ([1, 2, 3, 4, 5], [1], [2, 2, 3, 4, 5]),
            ([0], [0], [0]),
            ([9, 9, 9, 9, 9], [9, 9], [8, 9, 0, 0, 0, 1]),
            ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ],
    )
    def test_AddTwoNumbers(self, list1, list2, target):
        d1 = ListNode(0)
        t1 = d1
        for data in list1:
            t1.next = ListNode(data)
            t1 = t1.next

        d2 = ListNode(0)
        t2 = d2
        for data in list2:
            t2.next = ListNode(data)
            t2 = t2.next

        d0 = ListNode(0)
        targetNode = d0
        for data in target:
            targetNode.next = ListNode(data)
            targetNode = targetNode.next
        targetNode = d0.next

        sol = AddTwoNumbers()
        result = sol.addTwoNumbers(d1.next, d2.next)
        assert result.val == targetNode.val
        while result.next:
            result = result.next
            targetNode = targetNode.next
            assert result.val == targetNode.val
        assert result.next is None
        assert targetNode.next is None
