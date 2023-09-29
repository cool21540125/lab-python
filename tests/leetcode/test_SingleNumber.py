from leetcode.SingleNumber import Solution as SingleNumber
import pytest


# https://leetcode.com/problems/single-number/
class TestSingleNumber:
    @pytest.mark.parametrize(
        "nums, expected", [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)]
    )
    def test_singleNumber(self, nums, expected):
        s = SingleNumber()
        result = s.singleNumber(nums)
        assert (
            result == expected
        ), f"nums: {nums} expected to be {expected}, but got {result}"
