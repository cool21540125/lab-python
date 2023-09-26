from leetcode.SingleNumberIII import Solution as SingleNumberIII
import pytest

data1 = ([1, 2, 1, 3, 2, 5], [3, 5])
data2 = ([-1, 0], [0, -1])
data3 = ([0, 1], [0, 1])
data4 = ([1, 1, 3, 3, 5, 6], [5, 6])
data5 = ([-283, -174, 44, -174, 40, 40, 101, 101, 354, -283, 513, 513], [354, 44])


class TestSingleNumberIII:
    @pytest.mark.parametrize("nums, expected", [data1, data2, data3, data4, data5])
    def test_singleNumberiii(self, nums, expected):
        s = SingleNumberIII()
        result = s.singleNumber(nums)
        assert result == expected
