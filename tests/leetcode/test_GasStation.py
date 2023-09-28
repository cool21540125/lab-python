from leetcode.GasStation import Solution as GasStation
import pytest


class TestGasStation:
    @pytest.mark.parametrize(
        "gas, cost, expected",
        [
            ([3, 1, 2], [5, 2, 2], -1),
            ([3, 2, 1], [3, 2, 1], 0),
            ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
            ([2, 3, 4], [3, 4, 3], -1),
            ([5, 8, 2, 8], [6, 5, 6, 6], 3),
        ],
    )
    def test_GasStation(self, gas, cost, expected):
        station = GasStation()
        result = station.canCompleteCircuit(gas, cost)
        assert result == expected
