from leetcode.AddTwoNumbers import Solution, LinkedList
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
        ln1 = LinkedList(list1)
        ln2 = LinkedList(list2)
        target_node = LinkedList(target).listnode

        sol = Solution()
        result = sol.addTwoNumbers(ln1.listnode, ln2.listnode)
        assert result == target_node
