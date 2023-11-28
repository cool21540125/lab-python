from leetcode.MaximumAverageSubarrayI import Solution as MaximumAverageSubarrayI

import pytest


# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
class TestMaximumAverageSubarrayI:
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 12, -5, -6, 50, 3], 4, 12.75),
            ([5], 1, 5.0),
            ([1, 2, 3, 4, 5, 6, 7, 8], 3, 7),
            ([-1, -2, -3, -4, -5, -6, -7, -8], 3, -2),
            ([0, 0, 0, 8, 1, -1, -3], 3, 3),
        ],
    )
    def test_MaximumAverageSubarrayI(self, nums, k, expected):
        sol = MaximumAverageSubarrayI()
        result = sol.findMaxAverage(nums, k)
        assert (
            result == expected
        ), f"nums: {nums} expected to be {expected}, but got {result}"
