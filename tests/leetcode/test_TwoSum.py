from leetcode.TwoSum import Solution as TwoSum
import pytest


# https://leetcode.com/problems/two-sum/
class TestTwoSum:
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([3, 3], 6, [0, 1]),
            ([3, 4, 5, 6], 7, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([2, 7, 11, 15], 9, [0, 1]),
            ([2, 7, 11, 15], 18, [1, 2]),
            ([3, 6, 9, 12, 15], 27, [3, 4]),
        ],
    )
    def test_twoSum(self, nums, target, expected):
        s = TwoSum()
        result = s.twoSum(nums, target)
        assert (
            result == expected
        ), f"nums: {nums} & target: {target}, expected to be {expected}, but got {result}"
