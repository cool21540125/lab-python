from leetcode.SingleNumberIII import Solution as SingleNumberIII
import pytest


# https://leetcode.com/problems/single-number-iii/
class TestSingleNumberIII:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 1, 3, 2, 5], [3, 5]),
            ([-1, 0], [0, -1]),
            ([0, 1], [0, 1]),
            ([1, 1, 3, 3, 5, 6], [5, 6]),
            ([-283, -174, 44, -174, 40, 40, 101, 101, 354, -283, 513, 513], [354, 44]),
        ],
    )
    def test_singleNumberiii(self, nums, expected):
        s = SingleNumberIII()
        result = s.singleNumber(nums)
        assert result == expected, f"{nums} expected to be {expected}, but got {result}"
