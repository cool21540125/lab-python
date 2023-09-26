from leetcode.SingleNumber import Solution as SingleNumber
import pytest


class TestSingleNumber:
    @pytest.mark.parametrize(
        "nums, expected", [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)]
    )
    def test_singleNumber(self, nums, expected):
        s = SingleNumber()
        result = s.singleNumber(nums)
        assert result == expected
